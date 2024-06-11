# Description: This is the main file for the Streamlit app. It will be used to run the app.
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

## Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries"),
        ("user","Question:{question}"),
    ]

)

##streamlit framework

st.title("Langchain demo with openai api")
input_text=st.text_input("Enter your question")

# openai llm
llm=ChatOpenAI(model="gpt-3.5-turbo")

#responsuble for generating the response
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

#this if statement is responsible for generating the response meaning if the input_text is not empty then it will generate the response
if input_text:
    st.write(chain.invoke({"question":input_text}))