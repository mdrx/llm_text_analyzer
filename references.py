systemprompts = {
    "meeting": {
        "short_description": "Meeting summary",
        "system_prompt": 
    """You're an efficient and detail oriented executive assistant. You never make things up and you only base your output on available context. Answer the following question based ONLY on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""",
        "default_question": "Summarize the meeting and itemize any actions agreed, including responsible parties and timelines",
        "selected": True
    },
    "text": {
        "short_description": "Text summary",
        "system_prompt": """Forget everything about books. Books don't exist. Answer the following question based ONLY on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""",
        "default_question": "Outline the setting described and any characters mentioned. If there is a discernible plot, describe the most significant plot elements in detail.",
        "selected": False
    }
}

availablemodels_old = {
    'dolphin-llama3': {
        "short_description": "a finetuned version of llama3 with less censoring and more instruction obedience",
        "selected": True
    },
    'llama3': {
        "short_description": "base 8g version as published by Meta",
        "selected": False
    },
}



import ollama


availablemodels = {entry['name']: {'short_description': str(entry['details'])} for entry in ollama.list()['models']}
#for entry in ollama.list()['models']:
#    
#    
#    print(f"{entry['name']}, details: {str(entry['details'])}")
print(availablemodels)