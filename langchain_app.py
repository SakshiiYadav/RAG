import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from IPython.display import Markdown as md

# Setup API Key
f = open('C:/Users/saidu/OneDrive/Desktop/RAG/key.txt')
GOOGLE_API_KEY = f.read()

chat_model = ChatGoogleGenerativeAI(google_api_key=GOOGLE_API_KEY, model="gemini-1.5-pro-latest")

st.header("RAG System")

embedding_model = GoogleGenerativeAIEmbeddings(google_api_key=GOOGLE_API_KEY, model="models/embedding-001")

chat_template = """
    You are a Helpful AI Bot. 
    Welcome to the RAG System for "Leave No Context Behind" Paper. 
    As a RAG AI, your task is to provide insightful answers based on the context provided.
"""

st.write(chat_template)

# Function to interactively ask questions and get responses
def ask_question(context, question):
    st.write(f"**Context:** {context}")
    st.write(f"**Question:** {question}")
    answer = chat_model.get_response(context=context, question=question)
    st.write(f"**Answer:** {answer}")

# Example usage
context = "This is an example context."
question = "What is the main theme of the paper?"
ask_question(context, question)
