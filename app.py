import streamlit as st
import requests
import random
import hashlib

st.set_page_config(page_title="TalentScout Hiring Assistant")

hf_api_key = st.secrets["huggingface_api_key"]

# Set up Hugging Face API
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-alpha"
HEADERS = {"Authorization": f"Bearer {hf_api_key}"}  # API Key from secrets


# Apply Dark Theme Styling
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }
        .stTextInput, .stTextArea, .stSlider, .stButton {
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #bb86fc;
            color: white;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #3700b3;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# Tech stack categories
TECH_CATEGORIES = {
    "Python": "General programming, scripting, data structures, OOP",
    "TensorFlow": "Machine learning, neural networks, deep learning architectures",
    "PyTorch": "Deep learning, model training, optimization techniques",
    "React": "Frontend development, state management, component lifecycle",
    "Node.js": "Backend development, event-driven programming, APIs",
    "SQL": "Database management, query optimization, indexing",
    "AWS": "Cloud computing, deployment, scalability",
    "Docker": "Containerization, CI/CD, microservices",
    "Linux": "System administration, shell scripting, networking",
}


def classify_tech_stack(tech_stack):
    """Categorizes the given tech stack based on predefined categories."""
    categories = []
    for tech in TECH_CATEGORIES:
        if tech.lower() in tech_stack.lower():
            categories.append(TECH_CATEGORIES[tech])
    return ", ".join(categories) if categories else "General software development"


def anonymize_data(data):
    """Hashes sensitive user data to ensure privacy compliance."""
    return hashlib.sha256(data.encode()).hexdigest()


def generate_question(tech_stack, cnt):
    """Generates a technical interview question based on the tech stack and question number."""
    tech_category = classify_tech_stack(tech_stack)

    prompts = {
        1: f"Generate a basic technical interview question for a candidate skilled in {tech_stack}. "
           f"The question should be related to {tech_category}. Focus on basic concepts."
           "In no more than 250 words",

        2: f"Generate an intermediate technical interview question for a candidate skilled in {tech_stack}. "
           f"Ensure the question covers {tech_category} and includes a practical scenario."
           "In no more than 250 words",

        3: f"Generate an advanced technical interview question for a candidate skilled in {tech_stack}. "
           f"Focus on {tech_category} with a real-world problem or case study."
           "In no more than 250 words",

        4: f"Generate a very advanced technical interview question for a candidate skilled in {tech_stack}. "
           f"Ensure it challenges the candidate on {tech_category} optimization and problem-solving."
           "In no more than 250 words",

        5: f"Generate an expert-level technical interview question for a candidate skilled in {tech_stack}. "
           f"The question should assess expertise in {tech_category}, scalability, and design thinking."
           "In no more than 250 words",
    }

    prompt = prompts.get(cnt, prompts[1])
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    print("API Response:", response.json())

    if response.status_code == 200:
        generated_text = response.json()[0].get("generated_text", "").strip()
        if generated_text:
            split_text = generated_text.split("250 words, ")
            if len(split_text) > 1:
                after_250_words = split_text[1].strip()
                return after_250_words[0].upper() + after_250_words[1:] if after_250_words else ""
            else:
                return generated_text[0].upper() + generated_text[1:] if generated_text else ""
        else:
            return "Error: No valid question generated"
    else:
        return f"Error: {response.json()}"


def main():
    

    st.title("🤖 TalentScout Hiring Assistant")
    st.write(
        "Hello! I am here to help you with your job application process. Please provide your details and tech stack, and I will generate relevant interview questions for you! ")

    # Initialize session state if not already initialized
    if "exit" not in st.session_state:
        st.session_state["exit"] = False  
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []
    if "questions" not in st.session_state:
        st.session_state["questions"] = []
    if "answers" not in st.session_state:
        st.session_state["answers"] = {}
    if "follow_up" not in st.session_state:
        st.session_state["follow_up"] = ""

    # Collect candidate details
    st.subheader("📋 Candidate Information")
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.slider("Years of Experience", 0, 30, 1)
    position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Enter your tech stack (e.g., Python, TensorFlow, React)")

    # Submit button
    if st.button("Submit Information"):
        st.session_state["candidate_info"] = {
            "Full Name": full_name,
            "ID": anonymize_data(email + phone),
            "Experience": experience,
            "Position": position,
            "Location": location,
            "Tech Stack": tech_stack
        }
        st.success("Your details have been securely recorded!")

        if tech_stack:
            try:
                num_questions = random.randint(3, 5)
                questions = []
                answers = {}
                for i in range(num_questions):
                    question = generate_question(tech_stack, i + 1)
                    questions.append(question)
                    answers[i] = ""
                st.session_state["questions"] = questions
                st.session_state["answers"] = answers
                st.subheader("📌 Technical Questions")
                for idx, question in enumerate(questions):
                    st.write(f"Question {idx + 1}: {question}")
                    st.session_state["answers"][idx] = st.text_area(f"Your Answer to Question {idx + 1}")
            except Exception as e:
                st.error(f"Error generating questions: {e}")

    # Handle follow-up queries
    follow_up = st.text_input("Ask about a specific question (e.g., 'Clarify question 2'):")
    if follow_up:
        try:
            question_num = int(''.join(filter(str.isdigit, follow_up))) - 1
            if 0 <= question_num < len(st.session_state["questions"]):
                st.session_state["follow_up"] = f"Clarification for Question {question_num + 1}: {st.session_state['questions'][question_num]}"
            else:
                st.session_state["follow_up"] = "Invalid question number. Please ask about a valid question."
        except ValueError:
            st.session_state["follow_up"] = "Please specify a valid question number."
    if st.session_state["follow_up"]:
        st.write(st.session_state["follow_up"])

    # Fallback Mechanism
    user_input = st.text_input("Type here (or type 'exit' to end):")
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.session_state["exit"] = True
        st.write("Thank you for using TalentScout! Have a great day! 👋")
    elif user_input.strip():
        st.session_state["conversation"].append(user_input)
        st.write("I'm not sure I understand. Try asking about a question or type 'help' for guidance.")
    if st.session_state["exit"]:
        st.stop()


if __name__ == "__main__":
    main()
