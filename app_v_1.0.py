# CSV to SQL query generator+
    # This is a PAF project focussing on SQL query generation
    # Input in a CSV data sheet,
    # Ask the query, choose if you want an explanation or not, and get the query

# Features:
    # Input CSV
    # Type Table name
    # Structure of the data
    # Toggle for query explanation
    # Code snippet query 
    # Get the data from different data sources


import streamlit as st
import os
import langchain
import openai
import pandas as pd
import numpy as np
from pandasql import sqldf


# from OPENAI_API_KEY import OPENAI_API_KEY

st.subheader("Enter your OpenAI API Key")
OPENAI_API_KEY = st.text_input(" ", type="password")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

st.title("RD Query Generator")

# Runner functions

def llm_runner_3(user_query):
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        table,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    prompt_template = f"You are a MySQL query generator, specifically designed to read the data and then create semantically correct sql queries, the table will always be '{table_name}' keep this in context while designing the query. With that context, create an sql query to: "

    prompt = prompt_template + user_query

    if user_query:
        response = agent.run(prompt)
        sql_query = response[response.find("SELECT") : response.rfind("```")]
        st.code(sql_query, language='sql')
    
    return(sql_query)


def llm_runner_4(user_query):
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-4-1106-preview"),
        table,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    prompt_template = f"You are a MySQL query generator, specifically designed to read the data and then create semantically correct sql queries, the table will always be '{table_name}' keep this in context while designing the query. With that context, create an sql query to: "

    prompt = prompt_template + user_query

    if user_query:
        response = agent.run(prompt)
        sql_query = response[response.find("SELECT") : response.rfind("```")]
        st.code(sql_query, language='sql')

    return(sql_query) 


def explainer(sql_query):
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-4-1106-preview"),
        table,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    prompt = f"You are a MySQL query generator, specifically designed to read the data and then create semantically correct sql queries, Explain the purpose of the provided SQL query '{sql_query}'. Share details about the tables it utilizes, the key conditions, and what output it's designed to generate. Additionally, break down the logic and steps employed in the query to help me grasp its functionality better. The query is '{sql_query}'. The entire explanation should be in very concise, structured and relevant and uses simple english sentences and words, and the response should be markdown structured."

    response = agent.run(prompt)

    with st.expander("Explanation"):
        st.markdown(response)

mode = st.radio(
    "Data source",
    ["Import CSV", "Import XLSX"])

if mode == "Import CSV":
    uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

    table_name = st.text_input("Give your table a name (default `table`)")
    if not table_name:
        table_name = "Table"

    if uploaded_file:
        with st.expander("Structure of the data"):
            table = pd.read_csv(uploaded_file)
            st.subheader("Data Sample:")
            st.write(table.head())
            st.subheader("Data Structure (Rows, Columns):")
            st.markdown(table.shape)
            st.subheader("Data Attributes (Columns):")
            st.write(table.columns)
        
        user_query = st.text_input(
        "What type of SQl query do you need?",
        placeholder="For ex. 'Find the average age of passengers who survived and were in the first class.'",
        )

        generate = st.button("Generate Query")
        
        if generate and user_query and OPENAI_API_KEY:

            col1, col2= st.columns(2)

            with col1:
                st.markdown("### gpt 3.5 turbo")
                sql_query_3 = llm_runner_3(user_query)

            with col2:
                st.markdown("### gpt 4")
                sql_query_4 = llm_runner_4(user_query)

            col3, col4= st.columns(2)

            with col3:
                explainer(sql_query_3)

            with col4:
                explainer(sql_query_4)









































elif mode == "Import XLSX":
    uploaded_file = st.file_uploader("Choose a XLSX file", type='xlsx')

    table_name = st.text_input("Give your table a name (default `table`)")
    if not table_name:
        table_name = "Table"

    if uploaded_file:
        with st.expander("Structure of the data"):
            table = pd.read_excel(uploaded_file)
            st.subheader("Data Sample:")
            st.write(table.head())
            st.subheader("Data Structure (Rows, Columns):")
            st.markdown(table.shape)
            st.subheader("Data Attributes (Columns):")
            st.write(table.columns)

        user_query = st.text_input(
        "What type of SQl query do you need?",
        placeholder="For ex. 'Find the average age of passengers who survived and were in the first class.'",)
        generate = st.button("Generate")
        
        llm_runner(user_query)

