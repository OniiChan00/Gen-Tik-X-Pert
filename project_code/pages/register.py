import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import json
import requests



## uri = "mongodb+srv://Phoo:EWAH1KnfoMHEj99s@test-db.s72ptka.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
##client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
##try:
##    client.admin.command('ping')
##    print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
#        print(e)
#print(client.list_database_names())*/

code = 0

def register(user_data):
    #user_data = json.dump(user_data)
    #db = client["test"]
    #users_col = db["users"]
    #users_col.insert_one(user_data)
    #print("successfully Register")
    print(user_data)
  
    url = "http://192.168.1.106:8765/API/create_users"
  
    status = requests.post(url, data = user_data)
    code = status.status_code
    #print(code)
    if (code == 200):
        switch_page("login")
        print(code)
    elif (code == 201):
        switch_page("register")



def main():

    st.markdown("""
    <style>
    .big-font {
    font-size:25px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Register</p>', unsafe_allow_html=True)   
    username = st.text_input("Username")
    Email = st.text_input("Email")
    password = st.text_input("Password",type="password")
    check_password = st.text_input("Retype password",type="password")
    if(password ==  "" and check_password == ""):
        st.write("Please input password")
    elif(password != check_password):
        st.write("Password not match")
    else:
        st.write("Password Match")
    button = st.button("continue",type="secondary")
    if(button):
        register( {"Username": username,
                "Password": password,
                "Email": Email})
    

main()