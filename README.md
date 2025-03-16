# TalentScout Hiring Assistant

## 📌 Project Overview
TalentScout Hiring Assistant is an AI-powered chatbot designed to generate **context-aware technical interview questions** based on a candidate's tech stack. It enhances the hiring process by providing:
- **Dynamically generated technical questions** (Basic to Expert levels).
- **Context handling** for follow-up queries.
- **Privacy-focused data handling** (anonymization of sensitive data).
- **A sleek dark-themed UI** for a professional experience.

## 🚀 Live Demo
Try out the chatbot here: [TalentScout Hiring Assistant](https://hiringassistantchatbot.streamlit.app/)

## 🛠️ Installation Instructions
### Prerequisites
- Python 3.8+
- Streamlit
- Requests
- Hugging Face API Key (Create your own at [Hugging Face](https://huggingface.co/join))
  
### Setup & Run
### **1️⃣ Clone the Repository**
```bash
git clone [(https://github.com/knight22-21/Hiring_Assistant_chatbot)]
cd Hiring_Assistant_chatbot
```

### **2️⃣ Set Up a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Hugging Face API Key**
> **⚠️ IMPORTANT:** You must create your own Hugging Face API key.
1. Sign up at [Hugging Face](https://huggingface.co/join) if you don’t have an account.
2. Generate an API key from [your account settings](https://huggingface.co/settings/tokens).
3. Store the key securely by creating a `.streamlit/secrets.toml` file:

```toml
# .streamlit/secrets.toml
huggingface_api_key = "your_huggingface_api_key_here"
```

### **5️⃣ Run the Application**
```bash
streamlit run app.py
```

---

## 📝 Usage Guide
1️⃣ **Enter candidate details** (name, email, experience, tech stack, etc.).
2️⃣ **Get AI-generated technical questions** based on the candidate's expertise.
3️⃣ **Answer questions** directly in the chat UI.
4️⃣ **Ask follow-up queries** for clarifications.
5️⃣ **Clear session data** to ensure privacy compliance.

---

## 🔍 Technical Details
### **🛠️ Libraries Used**
- **Streamlit** – For the interactive UI.
- **Requests** – To communicate with the Hugging Face API.
- **Hashlib** – To anonymize candidate data.
- **Random** – For dynamic question variations.

### **🤖 Model Details**
- **Model Used:** `HuggingFaceH4/zephyr-7b-alpha`
- **Hosted on:** Hugging Face Inference API
- **Architecture:** Transformer-based large language model.

---

## 🎯 Prompt Design Strategy
- **Context-Aware Prompts:** Ensures question relevance based on tech stack.
- **Difficulty Scaling:** Ranges from **Basic** to **Expert-Level** questions.
- **Structured Format:** Forces AI to return **5 numbered questions** without unnecessary text.
- **Fallback Handling:** Provides meaningful responses to unexpected inputs.


---

## 🔥 Challenges & Solutions
### 1️⃣ API Rate Limits
- **Issue:** Hugging Face API sometimes throttles requests.
- **Solution:** Cached responses and added retries to prevent failures.

### 2️⃣ Ensuring Relevant Questions
- **Issue:** Generic questions from LLMs.
- **Solution:** Mapped tech stacks to predefined **categories** for **better prompt engineering**.

### 3️⃣ Secure Data Handling
- **Issue:** Sensitive data exposure.
- **Solution:** Used **SHA-256 hashing** for anonymization.

---


## 💡 Future Enhancements
🔹 **Integrate GPT-based models** for more advanced question evaluation.  
🔹 **Add answer feedback** using AI-based scoring.  
🔹 **Improve UI/UX** with animations and interactive components.  

---


🔗 **For Issues & Contributions:** Submit a PR or open an issue in the repository!
📩 Contact: krishnatyagi2526@gmail.com
