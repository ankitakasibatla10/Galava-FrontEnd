import streamlit as st
import pandas as pd
import yaml
from getKey import  get_secret
from getObjects import getDatabaseCredentials
from databaseClient import create_database_connections

# Streamlit app layout
st.title('My Streamlit App')

# Taking inputs
SecretName = st.text_input('Secret Name')
access_id = st.text_input('Access ID')
secret_access_id = st.text_input('Secret Access ID')

# Button to trigger the function
if st.button('Run Function'):
    secretval= get_secret(SecretName)
    dbCredentials = getDatabaseCredentials(secretval)
    yaml_data = yaml.safe_load(dbCredentials)

    with open('data.yaml', 'w') as file:
        yaml.dump(yaml_data, file, default_flow_style=False)

    database_connections = create_database_connections('data.yaml')

    print(database_connections)


    
