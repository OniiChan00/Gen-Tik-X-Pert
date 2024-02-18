import streamlit as st
import random
import requests
import json
import extra_streamlit_components as stx
import datetime
from streamlit_extras.switch_page_button import switch_page


def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()
cookies = cookie_manager.get_all()


def save():
    url = "http://192.168.1.106:8765/API/Save_Story"
    status   = requests.post(url, data = {
        "Username": st.session_state.Username,
        "instruction": st.session_state.topic,
        "input" : st.session_state.input,
        "output" : st.session_state.output
    },headers={'Accept': 'application/xml; charset=utf-8','User-Agent':'foo'}).json()


def fetch_data(topic):
    url = "http://192.168.1.106:8765/API/sample_data"
    status   = requests.post(url, data = topic,headers={'Accept': 'application/xml; charset=utf-8','User-Agent':'foo'}).json()
    #print(status)
    code = status["response"]
    #print(status)
    if (code == 200):
        story = status["data"]
        st.session_state['input'] = story["input"]
        st.session_state['output'] = story["output"]
        st.session_state['previous'] = st.session_state.topic
        #topic = status.data["input"]
        #data = status.data["output"]
        pass
    elif (code == 201):
        pass
      
def change():
    change = 1



def main():
    
    '''
    st.title("")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user","content": prompt})
        st.chat_message("user").write(prompt)
        st.session_state.messages.append({"role": "assistant", "content": word[random.randint(0,3)]})
        st.chat_message("assistant").write(word[random.randint(0,3)])
    '''
    
   
    
    st.sidebar.markdown("<h3 style='text-align: center; padding-top: 2vh;position:absolute'>Muchima Janpanich</h3>", unsafe_allow_html=True)
   
    st.title("Gen-Tik-X-Pert")
    st.session_state['topic']  = st.selectbox(
    'เลือกหมวดหมู่',
    ('เขียนสคริปต์รีวิวเครืองสำอาง', "Storytelling(Sci-fi)", "สคริปต์ Podcast (Sci-fi)",'อื่นๆ') )
    
    click = st.button('Next')
    if click:
        st.session_state.btn_state = True
        click = True
    
    try:
        if(st.session_state.btn_state):
            print(st.session_state['topic'])
            print(st.session_state['previous'])
            st.session_state['previous'] = st.session_state['topic']
            
            if(st.session_state.btn_state != True or click == True ):
                fetch_data({"topic":st.session_state['topic']})
                click = False

            st.session_state['input']  = head = st.text_input('Title', st.session_state.input or " ")
            st.session_state['output'] = text = st.text_area(
            "Input Pompt",
            st.session_state.output or " ",height=500
            )
            
            st.session_state.generate = st.button("Generate")
            if(st.session_state.generate):
                save()
                switch_page("audio")
    except:
        pass



if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'

hide_bar = """
           <style>
           [data-testid='collapsedControl"] {visibility:hidden;}
           </style>
           """

login_after = False



st.session_state['previous'] = ""  
main()
