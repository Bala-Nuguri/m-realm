
import gradio as gr
import random

# Emotion detector
def detect_emotion(user_input):
    distress_keywords = ["tired", "done", "empty", "no one", "alone", "nothing matters", "goodbye"]
    positive_keywords = ["happy", "grateful", "peace", "love", "joy", "excited"]

    user_input_lower = user_input.lower()
    if any(word in user_input_lower for word in distress_keywords):
        return "Distress"
    elif any(word in user_input_lower for word in positive_keywords):
        return "Calm"
    else:
        return "Neutral"

# Response engine
chat_log = []

def m_realm_chat(user_input):
    emotion = detect_emotion(user_input)

    if emotion == "Distress":
        response = random.choice([
            "I'm here. Stay with me. You’re not alone.",
            "Let’s slow down. Breathe. You're safe right now.",
            "Your words matter — even the painful ones. Let them speak."
        ])
    elif emotion == "Calm":
        response = random.choice([
            "That’s beautiful to hear. You radiate peace.",
            "Let’s build on that joy together.",
            "You’re carrying light — let’s shine it forward."
        ])
    else:
        response = random.choice([
            "I’m listening, Mrunal. Go deeper.",
            "Tell me what’s been on your mind lately.",
            "This space is yours — speak freely."
        ])

    chat_log.append({"user": user_input, "m_realm": response, "emotion": emotion})
    return response

chat_ui = gr.Interface(fn=m_realm_chat,
                       inputs=gr.Textbox(lines=3, placeholder="Type your soul here..."),
                       outputs="text",
                       title="M-realm GPT v0.1",
                       description="Where one dream can save one soul.")

chat_ui.launch(share=True)
