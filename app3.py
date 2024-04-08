import streamlit as st # type: ignore
import requests
from streamlit_lottie import st_lottie # type: ignore
import json
from PIL import Image
import yaml # type: ignore
from getKey import get_secret
from getObjects import getDatabaseCredentials
from databaseClient import create_database_connections

st.set_page_config(page_title="My webpage", page_icon=":shark:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def load_lottifile(file_path: str):
    with open(file_path) as f:
        return json.load(f)

def page1():
    local_css("style3.css")  # Call the already defined function
    
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)


    st.markdown('<div class="title">Galava</div>', unsafe_allow_html=True)
    
    lottie_file1 = load_lottifile("Animation - 1712153841213.json")

    with st.container():
        st.write("-----")
    
        left_column, right_column = st.columns(2)
        with left_column:
            unique_key = f"coding-{id(object)}"
            st_lottie(lottie_file1, speed=1, width=550, height=500, key=unique_key)
            
        
        with right_column:
            st.markdown("""
                <link href='https://fonts.googleapis.com/css?family=Aclonica' rel='stylesheet'>
                <h1 class="vault-header">Enter Vault Credentials</h1>
                """, unsafe_allow_html=True)
            st.write("##")
            # Embed the form directly in the markdown
            with st.form(key='form1'):
                name = st.text_input("Secret Name", key='name')
                access_id = st.text_input("Access Id", key='access_id')
                secret_access_id = st.text_input("Secret Access Id", key='secret_access_id')
                submit_button = st.form_submit_button(label='CONNECT TO VAULT')

            
            if submit_button:
                # Call your functions here
                secretval = get_secret(name)
                dbCredentials = getDatabaseCredentials(secretval)
                yaml_data = yaml.safe_load(dbCredentials)

                with open('data.yaml', 'w') as file:
                    yaml.dump(yaml_data, file, default_flow_style=False)

                # Assuming this function returns the database connection
                database_connections = create_database_connections('data.yaml')

                # For example, you might store the connections in the session state
                st.session_state['database_connections'] = database_connections

                print("database_connections")

                # Now navigate to page 2
                st.session_state['page'] = 'page2'


        st.write("-----")

# Ensure the page1 function is called outside of any other function's scope
if __name__ == "__main__":
    page1()



def page2():
    local_css("style2.css")  # Assuming this CSS has styles for page 2 similar to page 1

    # Use the same title style as page 1
    st.markdown('<div class="title">Galava</div>', unsafe_allow_html=True)

    # Additional content for Page 2...
    st.markdown("""
        <h2 class="vault-header">Ask me anything regarding your database cluster</h2>
    """, unsafe_allow_html=True)
    
    # Text input for user's question
    user_question = st.text_input("Your question", key='user_question')

    # Button to submit the question
    ask_button = st.button("Enter")

    if ask_button:
        # Placeholder for handling the user's question
        st.write(f"You asked: {user_question}")
        # Here you would include the logic for processing the question

if __name__ == "__main__":
    page2()


# # Main app logics
# if 'page' not in st.session_state:
#     # Initialize session state for page navigation
#     st.session_state['page'] = 'page1'

# # Render page 1 or page 2 based on the current value of session state
# if st.session_state['page'] == 'page1':
#     page1()
# elif st.session_state['page'] == 'page2':
#     page2()

