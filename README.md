# cmdash
### AI-powered Windows Command Line Assistant

cmdash is a lightweight AI helper for the Windows Command Prompt.
It gives you instant, context‑aware answers to command‑line questions without leaving your terminal or digging through documentation.

Ask it anything about Windows CMD commands, syntax, flags, or workflows and it will quickly give you a well-informed useful answer

### How it Works
cmdash uses the following process to answer user questions about the Windows Command Prompt
- a **batch file** (cmdash.cmd) captures the user prompt and runs a python file
- The python file constructs the user prompt, generates LLM system instructions, and calls the groq API for a response with the user prompt.
- The python file then does some error handling and prints the result to the screen (in this case, the windows command line)

### Why Use cmdash
cmdash provides a wide variety of helpful features to Windows command prompt users including:
- Instant help for CMD commands
- Support directly from Windows Command Prompt
- User-friendly interface requiring little to no knowledge of the command prompt
- Free to run using the extremely powerful groq free tier API

### Example Usage
A user first needs to follow the setup and installation instructions below.
Then, in windows command prompt (to open: press start, type "cmd", press enter), a user can use cmdash by typing "cmdash" followed by a prompt.

An example prompt is as follows:
```cmd
cmdash how do I search for a file in the current directory by name?
```
cmdash will then respond with an answer
```cmd
use this command: dir filename

This will list all files in the current directory that match the given filename, filename can be replaced with the name of the file you are searching for, and it also supports wildcards such as * and ? for more complex searches.
```

### Setup Instructions
1. Download the main.py file onto your Windows device somewhere on the main system drive (Usually the C: drive)
2. download the template batch file template.txt
3. copy and paste the file path for main.py into the template file where it says to insert the file path (replace the old text). Do not edit anything else in the template file.
4. save the template file in your home folder (C:Users\YourUserName\). Do not put it in a sub-folder. Rename the file to "cmdash.cmd".
5. Get a free API key from Groq. Go to groq.com, create an account (do not use an outlook email), click "API Keys", click "+ Create API Key", choose a display name and expiration date, continue and copy the generated API key.
6. Set the API in your Windows System Variables. Press start, type "Environment Variables" and press enter, click "Environment Variables", under user variables click "New...", set the variable name to "GROQ_API_KEY", paste the API key into the variable value field, click ok on everything.
7. Close command prompt if it is open
8. Open command prompt and use cmdash as explained above in the Example usage section. Enjoy!!
