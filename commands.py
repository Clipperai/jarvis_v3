import webbrowser
import datetime
from speaker import speak
import streamlit as st # type: ignore

# ===== Commands =====

def open_youtube():
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
        return "Opening YouTube"

def tell_time():
        t = datetime.datetime.now().strftime("%H:%M")
        speak(f"Time is {t}")
        return f"Time is {t}"


def run_command(command):
    
        if "youtube" in command:
               result =  open_youtube()
        
        elif "time" in command:
                result = tell_time()

        else:
            result = "Command not found"
            st.write(result)
            speak(result)

        return result
    