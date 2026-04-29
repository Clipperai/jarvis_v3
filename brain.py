from groq import Groq # type: ignore
import streamlit as st # type: ignore


client = Groq(api_key = st.secrets["GROQ_API_KEY"])

MODEL="openai/gpt-oss-safeguard-20b"

# ===== Groq =====

def ask_ai(prompt):
    response = client.chat.completions.create( 
                model = MODEL,
                messages = [{"role": "user", "content": prompt}]
            )
    
    return response.choices[0].message.content
