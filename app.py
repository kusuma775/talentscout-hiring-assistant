import streamlit as st
import ollama

# ---------------- UI ---------------- #

st.set_page_config(page_title="TalentScout Hiring Assistant")

st.title("🤖 TalentScout AI Hiring Assistant")
st.write(
    "Welcome! This assistant helps screen candidates by collecting essential details "
    "and generating technical interview questions based on your tech stack."
)

# ---------------- Session State ---------------- #

if "step" not in st.session_state:
    st.session_state.step = 0

if "candidate" not in st.session_state:
    st.session_state.candidate = {}

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Questions Flow ---------------- #

questions = [
    "👋 Welcome to TalentScout! Let's begin.\n\n👉 What is your **Full Name**?",
    "📧 Please provide your **Email Address**.",
    "📱 What is your **Phone Number**?",
    "💼 How many **years of experience** do you have?",
    "🎯 What **role(s)** are you interested in?",
    "📍 What is your **current location**?",
    "🧠 Great! Please list the **technologies you are comfortable with** so I can generate relevant technical questions."
]

keys = [
    "name",
    "email",
    "phone",
    "experience",
    "role",
    "location",
    "techstack"
]

# ---------------- Display Chat History ---------------- #

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Ask first question automatically
if len(st.session_state.messages) == 0:
    first_q = questions[0]
    st.session_state.messages.append({"role": "assistant", "content": first_q})
    st.chat_message("assistant").write(first_q)

# ---------------- User Input ---------------- #

user_input = st.chat_input("Type your response here...")

# Exit keywords
exit_words = ["exit", "quit", "bye", "goodbye"]

if user_input:

    # Check exit
    if user_input.lower() in exit_words:
        goodbye = "✅ Thank you for your time! Our recruitment team will review your profile and contact you for the next steps. Have a great day!"
        st.chat_message("assistant").write(goodbye)
        st.stop()

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    step = st.session_state.step

    # Save candidate info
    if step < len(keys):
        st.session_state.candidate[keys[step]] = user_input
        st.session_state.step += 1

    # Ask next question
    if st.session_state.step < len(questions):
        next_q = questions[st.session_state.step]
        st.session_state.messages.append({"role": "assistant", "content": next_q})
        st.chat_message("assistant").write(next_q)

    # 🔥 Generate Technical Questions
    else:

        techstack = st.session_state.candidate.get("techstack")

        prompt = f"""
You are TalentScout Hiring Assistant.

Generate 3 to 5 intermediate-level technical interview questions for EACH technology listed below.

Technologies:
{techstack}

Rules:
- Keep questions practical and assessment-focused
- Do NOT provide answers
- Format nicely
"""

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        questions_generated = response['message']['content']

        final_msg = f"""
✅ **Thank you! Here are your technical screening questions:**

{questions_generated}

🎉 That concludes the initial screening.

Our recruitment team will review your responses and reach out with next steps.
"""

        st.session_state.messages.append(
            {"role": "assistant", "content": final_msg}
        )

        st.chat_message("assistant").write(final_msg)

        # Stop further inputs
        st.session_state.step += 1


