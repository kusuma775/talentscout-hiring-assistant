# 🤖 TalentScout AI Hiring Assistant

An intelligent AI-powered Hiring Assistant chatbot designed to streamline the initial candidate screening process for TalentScout, a fictional technology recruitment agency.

This assistant interacts with candidates, collects essential information, and generates tailored technical interview questions based on their declared tech stack.

---

## 🚀 Project Overview

The TalentScout Hiring Assistant automates early-stage recruitment by:

✅ Gathering candidate details  
✅ Maintaining structured conversation flow  
✅ Generating technical screening questions  
✅ Ensuring context-aware interactions  
✅ Providing a professional hiring experience  

This project demonstrates practical implementation of **LLMs, prompt engineering, conversational control, and AI product thinking.**

---

## ⭐ Key Features

### ✅ Structured Conversation Flow
The chatbot guides candidates step-by-step to collect:

- Full Name  
- Email Address  
- Phone Number  
- Years of Experience  
- Desired Role  
- Current Location  
- Tech Stack  

This ensures predictable and professional interactions rather than behaving like a generic chatbot.

---

### ✅ AI-Powered Technical Question Generation
Once the candidate provides their tech stack, the assistant generates **3–5 intermediate-level technical interview questions** for each technology.

Example:

**Input:** Python, Django, MySQL  
**Output:** Role-relevant screening questions for each technology.

---

### ✅ Context-Aware Chat
The chatbot maintains conversation state using Streamlit session management, allowing it to:

- Handle follow-ups  
- Avoid repetitive questions  
- Provide coherent responses  

---

### ✅ Professional Hiring Tone
The assistant is designed to behave like a real recruitment tool:

- Structured  
- Concise  
- Purpose-driven  
- Non-deviating from hiring workflow  

---

## 🧠 Prompt Engineering Approach

Prompts were carefully designed to:

- Guide the model through controlled hiring stages  
- Prevent unrelated conversations  
- Generate practical technical questions  
- Maintain professional tone  
- Ensure consistent outputs across diverse tech stacks  

**System Prompt Strategy:**
- Role-based prompting  
- Task constraint instructions  
- Output formatting guidance  

This demonstrates applied understanding of real-world LLM orchestration.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI development  
- **Ollama (Local LLM)** – AI model execution  
- **Session State Management** – Conversation control  

---

## 📦 Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/hiring-assistant-chatbot.git
cd hiring-assistant-chatbot






