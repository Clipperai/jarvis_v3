import speech_recognition as sr

# ===== Listen =====
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        return r.recognize_google(audio).lower() # type: ignore
    except:
        return ""