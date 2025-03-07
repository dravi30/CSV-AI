import os
import streamlit as st
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
from langchain_google_genai import ChatGoogleGenerativeAI  # Gemini integration

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY is missing! Set it in the .env file.")
    exit(1)

st.set_page_config(page_title="CSV AI with Gemini 1.5 Pro")
st.header("Ask Your CSV with Gemini 1.5 Pro")

csv_file = st.file_uploader("Upload a CSV file", type="csv")

if csv_file is not None:

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GOOGLE_API_KEY)

   
    agent = create_csv_agent(
        llm, csv_file, verbose=True, allow_dangerous_code=True
    )

    
    user_question = st.text_input("Ask a question about your CSV:")

    if user_question:
        with st.spinner("Processing..."):
            response = agent.run(user_question)
            st.write(response)
