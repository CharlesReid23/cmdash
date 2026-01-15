# cmdash
CMDASH — AI-powered Windows Command Line Assistant

cmdash is a lightweight AI helper for the Windows Command Prompt.
It gives you instant, context‑aware answers to command‑line questions without leaving your terminal or digging through documentation.

Ask it anything about Windows CMD commands, syntax, flags, or workflows and it will quickly give you a well-informed useful answer

### How it Works
cmdash is built from a fairy simple pipeline
- a **batch file** (cmdash.cmd) captures the user prompt and runs a python file
- The python file constructs the user prompt, generates LLM system instructions, and calls the groq API for a response with the user prompt.
- The python file then does some error handling and prints the result to the screen (in this case, the windows command line)
