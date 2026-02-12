🤖 TalentScout — AI Hiring Assistant (LLM Screening Chatbot)

An intelligent AI-powered Hiring Assistant chatbot built for TalentScout, a fictional recruitment agency specializing in technology placements.

This chatbot supports early-stage candidate screening by collecting structured candidate details and generating 3–5 tailored technical questions based on the candidate’s declared tech stack.

📌 Project Overview

TalentScout Hiring Assistant automates the initial screening workflow by:

Greeting the candidate and explaining the purpose

Collecting essential candidate information

Asking the candidate to declare their tech stack

Generating technical screening questions per technology

Maintaining conversation context and flow

Handling fallback / unexpected inputs

Ending the conversation gracefully

This project demonstrates practical implementation of:

LLMs • Prompt Engineering • Context Handling • Conversational Control • AI Product Thinking

⭐ Key Features (Meets Assignment Requirements)
✅ 1) Clean UI (Streamlit)

Simple, recruiter-style interface

Chat-based interaction for candidates

Clear input + response flow

✅ 2) Greeting + Purpose + Exit Keywords

Greets candidates at the start

Explains the assistant’s screening purpose

Supports conversation exit keywords like:
exit, quit, stop, end, bye

✅ 3) Candidate Information Gathering

Collects the following details in a structured flow:

Full Name

Email Address

Phone Number

Years of Experience

Desired Position(s)

Current Location

Tech Stack

✅ 4) Tech Stack Declaration

Prompts candidates to provide their tech stack, including:

Programming languages

Frameworks

Databases

Tools / Platforms

Example input:
Python, Django, MySQL, Git, AWS

✅ 5) Technical Question Generation (3–5 per Tech)

Generates 3–5 intermediate-level technical questions for each technology mentioned.

Example:

Tech Stack: Python, Django, MySQL
Output: 3–5 questions per technology tailored to assess proficiency.

✅ 6) Context Handling (Coherent Flow)

Maintains conversation context using:

Streamlit session state

Stage-based conversation tracking

Avoids repetition

Handles follow-up responses smoothly

✅ 7) Fallback Mechanism

If the user provides unexpected input, the chatbot:

Responds professionally

Guides the candidate back to the correct flow

Does not deviate from the hiring purpose

✅ 8) End Conversation Gracefully

Ends the chat with:

Thank you message

Next steps info

Clear closure

🧠 Prompt Engineering (Purpose of Prompting)

Prompts were designed to ensure the model:

1) Collects candidate information

Controlled stage-by-stage prompting

Validation-friendly output formats

2) Generates relevant technical questions

Questions are tech-specific

Difficulty is intermediate-level

Output is structured and consistent

3) Maintains coherent and context-aware interactions

Model is instructed to stay within hiring workflow

Conversation remains purpose-driven

🧩 Prompt Design Strategy (What Makes It Work)
✅ System Prompt (Role + Constraints)

The system prompt defines:

Role: Hiring Assistant

Tone: professional recruiter-style

Scope: screening only

Rules: no deviation, no irrelevant chat

✅ Question Generation Prompt

Uses a structured format like:

Tech name

Difficulty

Output formatting

Count of questions

✅ Output Control

Prompts include:

formatting constraints

consistent question structure

stage-based logic

🏗️ Architecture (Simple)

UI Layer: Streamlit
LLM Layer: Ollama (Local LLM, e.g., llama3)
State Layer: Streamlit session_state
Flow Control: Stage-based screening pipeline

🛠️ Tech Stack

Python

Streamlit (Frontend UI)

Ollama (Local LLM)

Session State Management

Git + GitHub (version control)

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kusuma775/talentscout-hiring-assistant.git
cd talentscout-hiring-assistant
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Install & Run Ollama (Required)
Download Ollama from:

https://ollama.com/

Then run the model locally:

```bash
ollama run llama3
```

### 6️⃣ Run the Streamlit App
```bash
streamlit run app.py
```


🧪 Usage Guide
Candidate Flow

Candidate opens the chatbot

Assistant greets + explains purpose

Assistant collects candidate details

Candidate provides tech stack

Assistant generates 3–5 questions per technology

Assistant ends conversation politely

🔐 Data Handling & Privacy

This project follows privacy best practices:

Candidate data is not stored permanently

Data is kept in memory during the session only

No real user data is collected during development

Simulated/anonymized data used for testing

Designed to align with privacy principles (GDPR-style)

🧩 Challenges & Solutions
Challenge 1: Keeping the chatbot structured (not generic)

✅ Solution: Stage-based prompting + session state tracking.

Challenge 2: Generating relevant questions for diverse tech stacks

✅ Solution: Prompt format enforces tech-specific, intermediate-level questions.

Challenge 3: Handling unexpected inputs

✅ Solution: Fallback responses + flow redirection logic.

🧾 Version Control (GitHub Workflow)

Code maintained using Git

Clean commit history

Repository structured for readability and maintainability

Modular design for future extension


🚀 Optional Enhancements (Future Scope)

Resume parsing + scoring

Candidate scoring engine

Recruiter dashboard

Database integration

Multi-role hiring workflows

Cloud deployment (AWS/GCP)

👩‍💻 Author

Kurumu Kusuma
Aspiring AI/ML Engineer | Python Developer

🔗 LinkedIn: https://www.linkedin.com/in/kusumakurumu/

🔗 GitHub: https://github.com/kusuma775

⭐ If you found this project useful, consider giving it a star!


