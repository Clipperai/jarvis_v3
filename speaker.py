import pyttsx3
import pythoncom

def speak(text):
    engine = pyttsx3.init()

    try:
        pythoncom.CoInitialize()   # 🔥 FIX
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except:
        pass