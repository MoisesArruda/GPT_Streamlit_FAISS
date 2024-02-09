import glob
import os
from typing import List
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import LLMChain
from app.class_gpt import GPTConfig,PromptChunks,VectorStoreMemory
load_dotenv()

def gpt_input():

    llm_embeddings = GPTConfig().create_embeddings()
    pages = PromptChunks().create_pages(r'data/Containers_com_Docker.pdf')
    chunks = PromptChunks().create_chunks(pages)
    db = VectorStoreMemory().input_FAISS(chunks,llm_embeddings)

    return db


def gpt_anwser(query=None,db=None):
     
    llm_chat = GPTConfig().create_chat()
    prompt = PromptChunks().create_prompt()
    db = db
    contexto,memory = VectorStoreMemory().input_memory(db,query)
    llm_chain = LLMChain(llm=llm_chat,prompt=prompt,memory=memory,verbose=True)
    response = llm_chain.run(query=query,contexto=contexto,memory=memory)

    return response


#db = gpt_input()
#print(gpt_anwser("O que é o Docker?",db))


