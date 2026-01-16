# Groq-Assist

## AI-Powered Windows Command Prompt Helper

The idea is to be working in the windows command prompt and be able to ask groq how a given command works without having to pour though a manual or use an external AI like Copilot

It's completely free because it will use groq free tier

I also want it to be very knowledgeable so I want to have a large file full of command prompt or powershell documentation that it can look through to inform its answer

I think it would be good if a user calls the function by saying the name of the ai, so that could look like this...

```angular2html
groq [user prompt pertaining to windows cmd]
```

for instance a user types in something like



```angular2html
groq how do I search the current directory for a certain file name?
```

and groq would answer something like...

```angular2html
Use this code. replace filename.txt with the actual file name

dir filename.txt
```

Ok it's done!!!
I called it cmdash