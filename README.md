Project Overview : TalentScout Hiring Assistant Chatbot

TalentScout Hiring Assistant is an AI-powered, conversational chatbot designed to assist in the initial screening of candidates for technology roles.
The chatbot interacts with candidates in a chat-like interface, collects essential profile information, maintains conversational context, and generates personalized technical interview questions based on the candidate’s background and declared tech stack.

This project demonstrates:
Prompt engineering
Context-aware conversational flow
Responsible data handling
Clean UI design using Streamlit
Practical use of Large Language Models (LLMs)

Key Features :
1. Conversational Hiring Assistant
The chatbot interacts in a natural chat format rather than a traditional form.Bot responses acknowledge user inputs and guide the conversation step by step.Previous messages are preserved and displayed to maintain conversational continuity.

2. Candidate Information Collection
The chatbot collects the following information during the conversation:
Full Name
Email Address (validated)
Phone Number (validated)
Years of Experience (validated numeric input)
Desired Role
Current Location
Tech Stack (comma-separated)
Each step is context-aware and conversational.

3. Context-Aware Question Generation
Candidate details are stored in memory using Streamlit session state.A contextual prompt is dynamically constructed using:
Candidate name
Experience level
Desired role
Tech stack
Technical interview questions are generated based on this context, making them relevant to the candidate’s profile.

4. Local LLM Mode (TinyLLaMA)
To avoid external API dependencies and quota limitations, the application supports a local Large Language Model (LLM) mode using TinyLLaMA via Ollama.
Key Characteristics
Technical interview questions are generated locally on the user’s machine.
No API key or internet connection is required after the model is downloaded.
The model runs entirely on CPU and is suitable for low-resource systems.
Questions are generated once per session based on the candidate’s profile and tech stack.
The architecture is modular, allowing easy replacement with larger local models or cloud-based LLMs when system resources permit.

5. Clean and Focused UI Flow
After tech stack submission, the UI switches to a question-only view.Previous form-style prompts are hidden to keep the user focused.A styled question card improves readability and presentation.



Technology Stack
Programming Language: Python
Frontend Framework: Streamlit
LLM Integration: OpenAI-compatible interface (mock-enabled)
Environment Management: python-dotenv
Version Control: Git & GitHub
Prompt Engineering Strategy


Installation & Setup -Prerequisites
Python 3.9+
Git
Streamlit
ollama -tinyllama

steps to run the program:
1. git clone https://github.com/ThanushaMH/talentscout-chatbot.git
cd talentscout-chatbot
2. pip install -r requirements.txt
3. python -m streamlit run app.py

Challenges & Solutions
1. OpenAI API Quota Limitations
Challenge: API quota errors during development.
Solution: Implemented a mock LLM mode with randomized technical questions.

2. Maintaining Conversation State in Streamlit
Challenge: Streamlit reruns the script on every input.
Solution: Used st.session_state to persist conversation history and candidate data.

3. Chat History Inconsistencies
Challenge: Missing bot messages in chat display.As the model was too large to handel
Solution: Ensured all bot responses are stored in session-based chat history using a dedicated helper function. Switched from phi to tinyllama.