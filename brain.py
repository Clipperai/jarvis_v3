import requests


# ===== Local AI (Phi) =====
def ask_ai(prompt):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "phi", "prompt": prompt, "stream": False}
        )
        return res.json()["response"]
    except:
        return "AI not available"