# text_summarizer

summarize large amounts of text using langchain, ollama and flask. Spins out a local server using flask, works offline, no data leaves the computer.

## How to set up

- fork or clone repository
- recommended: create new environment with venv
- Install Ollama for easy interaction with LLMs (`brew install ollama`), follow instructions to spin up the ollama service
- download llm models, e.g.:
    `pull ollama dolphin-llama3`
    `pull ollama llama3`
    (feel free to add other models)
- navigate to the local folder of the repo
- install dependencies (`pip install -r requirements.txt`)

## How to use

- navigate to repo local folder, enter your venv environment if set up
- run `python app.py`
- - interface spins up in localhost, typically [http://127.0.0.1:5000] 
- - Open the link in your browser
- provide context to work from - either copy/paste or open a file (which will populate the input window)
- Select model to use - dropdown will list those that are available in ollama. For more info on models, visit [ollam library](https://ollama.com/library)
- you can pick from predefined system prompts and questions, or you can edit it. It is crucial to include {context} and {input} in the system prompt, as otherwise the model won't know what data to base the answer on, and what the question is
- Submit and... patience! Time depends hugely on your system performance and on size of the text
- You'll get the generated response and the request metadata in a page
