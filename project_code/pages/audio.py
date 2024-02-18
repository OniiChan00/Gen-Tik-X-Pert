import streamlit as st
import extra_streamlit_components as stx
from streamlit_extras.switch_page_button import switch_page
from gtts import gTTS
import randomname
import os


def main(): 

    message = st.session_state['output']
    name = randomname.get_name()
    tts = gTTS(text=message, lang='th', slow=False)
    #st.audio(tts)
    tts.save(name + '.wav')

    main_file =  open(name + ".wav", "rb").read()
    dest_file = open('./audio/' + name +  '.wav', 'wb+')
    dest_file.write(main_file)
    dest_file.close()
    os.remove(name + ".wav")
    

    audio_file = open('./audio/' + name +  '.wav', 'rb')
    audio_bytes = audio_file.read()
    st.session_state['output'] = text = st.text_area(
            "Input Pompt",
            message , height=500,disabled=True
    )
    st.audio(audio_bytes, format='audio/wav')

main()