# 🤖 TalentScout AI Hiring Assistant

An intelligent **AI-powered Hiring Assistant chatbot** designed to streamline the initial candidate screening process for TalentScout, a fictional technology recruitment agency.

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

**Example:**

**Input:** Python, Django, MySQL  
**Output:** Role-relevant screening questions for each technology.

---

### ✅ Context-Aware Chat
The chatbot maintains conversation state using **Streamlit session management**, allowing it to:

- Handle follow-ups  
- Avoid repetitive questions  
- Provide coherent responses  

---

### ✅ Professional Hiring Tone
The assistant is designed to behave like a real recruitment tool:

✔ Structured  
✔ Concise  
✔ Purpose-driven  
✔ Non-deviating from hiring workflow  

---

## 🧠 Prompt Engineering Approach

Prompts were carefully designed to:

- Guide the model through controlled hiring stages  
- Prevent unrelated conversations  
- Generate practical technical questions  
- Maintain professional tone  
- Ensure consistent outputs across diverse tech stacks  

### **System Prompt Strategy**
- Role-based prompting  
- Task constraint instructions  
- Output formatting guidance  

This demonstrates applied understanding of **real-world LLM orchestration.**

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
git clone https://github.com/kusuma775/talentscout-hiring-assistant.git
cd talentscout-hiring-assistant
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file and add your configuration if required.

Example:

```
MODEL=llama3
```

---

### 5️⃣ Run Ollama (Required)

Make sure Ollama is installed and running locally:

```
ollama run llama3
```

---

### 6️⃣ Launch the Application

```bash
streamlit run app.py
```

The app will open in your browser 🚀

---

## 📊 Example Workflow

1️⃣ Candidate opens chat  
2️⃣ Assistant collects professional details  
3️⃣ Candidate enters tech stack  
4️⃣ AI generates technical screening questions  
5️⃣ Recruiter gets structured candidate data  

---

## 🔐 Privacy & Security

- No candidate data is permanently stored  
- Environment variables protect sensitive configurations  
- Designed with responsible AI interaction principles  

---

## 🎯 Why This Project Matters

Modern recruitment is increasingly AI-assisted.

This project showcases the ability to:

✅ Build real-world AI applications  
✅ Control LLM behavior using prompt engineering  
✅ Design structured conversational systems  
✅ Think like an AI product developer  
✅ Deliver practical automation tools  

---

## 🔮 Future Improvements

- Resume parsing  
- Automated candidate scoring  
- Recruiter dashboard  
- Database integration  
- Multi-role hiring workflows  
- Deployment on cloud platforms  

---

## 👩‍💻 Author

**Kusuma Kurumu**  
Aspiring AI/ML Engineer | Python Developer  

🔗 LinkedIn: https://linkedin.com/in/YOUR-LINKEDIN  

---

## ⭐ If you found this project useful, consider giving it a star!








