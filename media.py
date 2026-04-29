import pywhatkit as kit
from speaker import speak
import streamlit as st # type: ignore

def play(cmd):
    kit.playonyt(cmd) # type: ignore
    st.write(f"Playing {cmd}")
    speak(f"Playing {cmd}")