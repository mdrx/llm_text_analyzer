# text_summarizer
summarize large amounts of text using langchain, ollama and flask. Spins out a local server using flask, works offline, no data leaves the computer

## Prerequisites

- recommended: create new environment with venv
- Ollama for easy interaction with LLMs (`brew install ollama`), follow instructions to spin up service
- download llm models:
    pull ollama dolphin-llama3
    pull ollama llama3
    (maybe add others)
- langchain, flask (pip install -r requirements.txt)

## How to use

- once the models are dopwnloaded, this works completely offline.
- run app.py in python
interface spins up in localhost, typically http://127.0.0.1:5000 
Open the link in browser
- provide context to work from - either copy/paste or open a file (which will populate the input window)
- Select model to use - dropdown will list those that are available in ollama. For more info on models, visit [ollam library](https://ollama.com/library)
- you can pick from predefined system prompts and questions, or you can edit it. It is crucial to include {context} and {input} in the system prompt, as otherwise the model won't know what to base the answer to, and what the question is
- Submit and... patience! For simple tasks, response is available within 30-60 seconds but with large text volumes, it can take much longer