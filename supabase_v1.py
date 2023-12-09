import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Initializing client
url: str = "https://pyfarhoxpotcfohlohii.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB5ZmFyaG94cG90Y2ZvaGxvaGlpIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwMTg0NjE3NSwiZXhwIjoyMDE3NDIyMTc1fQ.YEeeap8tpjfk3zumQ6T8f1wh0G_piiTfq58QppsPyYM"  # Replace with your API key
supabase: Client = create_client(url, key)

# Streamlit UI
st.title("Titanic Database Query Tool")

# Execute query and get data
def get_data():
    response = supabase.table('titanic_db').select("*").execute()
    return response.data

if st.button("Load Data"):
    with st.spinner('Loading data...'):
        data = get_data()
        # Convert to DataFrame for better display
        df = pd.DataFrame(data)
        st.dataframe(df)  # Display the data in the app

st.markdown("*Data from the Titanic database.*")
