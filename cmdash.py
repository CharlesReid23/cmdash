import os
import sys
from groq import Groq

#if the user just types in cmdash have an explanation of how it works
if len(sys.argv) == 1:
    print('Usage: cmdash <your question here>')
    print('Example: cmdash how do I search files recursively?')
    print()
    sys.exit()

#generate the prompt the user typed
user_prompt = ' '.join(sys.argv[1:]).strip()

#create system instructions to accompany the user prompt
system_instructions = '''
You are an expert in Windows Command Prompt (cmd.exe).
Answer the following prompt ONLY with the exact command or commands needed, plus a brief explanation.
Do not add greetings, markdown, or extra text.
Type the command first, then the explanation.
Have the command on a separate line from the explanation with an empty line in between.
'''

#load the api with the api key
client = Groq(api_key = os.getenv("GROQ_API_KEY"))

#generate the response while handling errors
try:
    response = client.chat.completions.create(
        model = 'llama-3.3-70b-versatile',
        messages = [
            {
                "role": 'system',
                'content': system_instructions,
            },
            {
                'role': 'user',
                'content': user_prompt
            }
        ],
        timeout = 5 #seconds
    )

except Exception as e:
    print(f'Unable to complete request due to {e}')
    print()
    sys.exit(1)

#print the generated response to the screen and an empty line for spacing
print(response.choices[0].message.content)
print()