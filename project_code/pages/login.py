import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import extra_streamlit_components as stx
import datetime
import requests
import json


def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()
cookies = cookie_manager.get_all()

def login_check(user_data):
    url = "http://192.168.1.106:8765/API/login"
    status   = requests.post(url, data = user_data,headers={'Accept': 'application/xml; charset=utf-8','User-Agent':'foo'}).json()
    print(type(status))
    
    #code = status["response"]
    code = status["response"]
    token = status["token"]
    username = status["Username"]


    if (code == 200):
        st.session_state["token"] = token
        st.session_state["Username"] = username
        switch_page("index")
    elif (code == 201):
        switch_page("login")

def main():
    st.markdown("""
    <style>
    .big-font {
    font-size:25px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Login</p>', unsafe_allow_html=True)   
    username = st.text_input("Username")
    password = st.text_input("Password",type="password")
    button = st.button("login",type="secondary")
    if(button):
        login_check({
            "Username": username,
            "Password": password
        })

main()