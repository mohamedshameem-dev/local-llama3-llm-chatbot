# 🤖 Local LLM Chatbot using Ollama & Llama3
## 📌 Overview
## This project is a fully local AI chatbot built using:

* Ollama
* Llama3 model
* Python

The chatbot is configured as an Ecommerce Payment Analyst Assistant. Developed by MrShameem

### 🎯 Purpose
This project demonstrates:
Local LLM deployment
AI integration using Python
Practical business use case (Ecommerce Payment Analysis)
Prompt engineering for domain-specific assistant
Ideal for showcasing AI + Business Analyst skills.

### 🏗 Project Architecture
* User Input
↓
* Python Chat Interface
↓
* Ollama Runtime
↓
* Llama3 Model (Local)
↓
* AI Response

## 🛠 Tech Stack
- Python 3.10+
- Ollama
- Llama3
- PowerShell
- VS Code

### Step 1: Install Ollama

Download from:
https://ollama.com/download

Verify installation:
ollama --version

### Step 2: Install Llama3 Model
ollama pull llama3
Test model:
ollama run llama3

### Step 3: Install Python Dependency
pip install ollama

### Step 4: Run Chatbot
python chatbot.py

### Recommended Model for 16GB RAM
Use:
- ollama pull llama3
- This pulls the 8B version (best balance of:
- Quality
- Speed
- RAM usage (~6–8GB)
- Then run:
- ollama run llama3
- If it responds → you’re good.

## Benefits:
100% FREE
100% Local
No API key
No billing

## Disclaimer:
Important Limitation (Current Version)
This version:
❌ Does NOT remember previous messages
Each question is independent.
If you want memory (real chatbot behavior), use upgraded version. Soon i will upload script with memory

## Give a thumbs up if you really liked and learnt something from here.





