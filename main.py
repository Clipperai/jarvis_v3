import streamlit as st # type: ignore
import time
from brain import ask_ai
from commands import run_command
import webbrowser


# ===== UI =====
st.title("Jarvis V3")

if "chat" not in st.session_state:
    st.session_state.chat = []

reply = ''
status = st.empty()
# ===== Buttons =====
if st.button("Press Me"):
    
        status.info("...")
    
        time.sleep(1)
        cmd = st.text_input("Enter command")
        if cmd:
                st.session_state.chat.append(("You:", cmd))
                status.info("🔍 Searching command...")
                
                time.sleep(2)

                if "exit" in cmd:
                    reply = "Goodbye"
                
                elif "youtube" in cmd:
                    run_command(cmd)
                
                elif "time" in cmd:
                    run_command(cmd)

                elif "play" in cmd:
                        status.info("🎶 Playing...")
                        time.sleep(1)
                        cmd = cmd.replace("play"," ").split()
                        webbrowser.open(f"https://www.youtube.com/results?search_query={cmd}")
                        
                else:
                        status.info("🧠 Thinking...")
                        
                        reply = ask_ai(cmd)
                        st.write(reply)
                        # speak(reply)

                status.success("✅ Done") 

        st.session_state.chat.append(("Jarvis", reply))

# ===== Chat Display =====
for sender, msg in st.session_state.chat:
    st.write(f"**{sender}** {msg}")
