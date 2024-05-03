from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import SentenceTransformersTokenTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import datetime

#from langchain_community.document_loaders import WebBaseLoader

def get_response(content, question, model, systemprompt):

    starttime = datetime.datetime.now()

    try:
        docs = [Document(page_content=content)]
    except Exception as e:
        return str(e)

    llm = Ollama(model=model)
    embeddings = OllamaEmbeddings(model=model)
    text_splitter = SentenceTransformersTokenTextSplitter()
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings)

    prompt = PromptTemplate.from_template(systemprompt)

    document_chain = create_stuff_documents_chain(llm, prompt)

    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    response = retrieval_chain.invoke({"input": question})

    return(
        {
            'response': response["answer"],
            'metadata': {
                'start time': starttime, 
                'stop time': datetime.datetime.now(), 
                'model used': model,
                'system prompt': systemprompt,
                'question (\{input\})': question,
                'context': content if len(content) < 100000 else content[:10000] + ' \n\n [rest hidden as too large]'
            }
        })

