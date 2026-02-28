import streamlit as st
from prompts import SYSTEM_PROMPT, TECH_QUESTION_PROMPT
from utils import get_llm_response
import re
def handle_input():
    st.session_state.last_input = st.session_state.input
    st.session_state.input = ""
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)
def next_step():
    st.session_state.step += 1
def bot_says(message):
    st.session_state.chat_history.append(
        {"role": "assistant", "content": message}
    )
    st.write(message)

st.set_page_config(page_title="TalentScout Hiring Assistant")

st.title("TalentScout Hiring Assistant")
st.info(
    "**Data Privacy Notice**\n\n"
    "The information you provide is used only for initial screening purposes. "
    "No data is stored permanently, shared with third parties, or used beyond this session."
)

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.data = {}
    st.session_state.show_questions = False
    st.session_state.prompt = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"🧑 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **TalentScout:** {msg['content']}")

exit_words = ["exit", "quit", "bye"]

st.text_input(
    "You:",
    key="input",
    on_change=handle_input
)

user_input = st.session_state.get("last_input", "")
if user_input:
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input})

    if user_input.lower() in exit_words:
        st.success("Thank you for your time! Our team will contact you soon.")
        st.stop()

    if st.session_state.step == 0:
        bot_says("Hi there!  I’m TalentScout. I will assist with your initial screening. Let's begin!! What’s your full name?")        
        st.session_state.step += 1

    elif st.session_state.step == 1:
        st.session_state.data["name"] = user_input
        bot_says(f"Nice to meet you, {user_input}! ")
        bot_says("What’s your email address?")       
        next_step()

    elif st.session_state.step == 2:
        if not is_valid_email(user_input):
         st.error("Please enter a valid email address.")
        else:
            st.session_state.data["email"] = user_input
            bot_says("Got it")
            bot_says("Could you share your phone number?")            
            next_step()

    elif st.session_state.step == 3:
            if not is_valid_phone(user_input):
                st.error("Phone number must be 10 digits.")
            else:
                st.session_state.data["phone"] = user_input
                bot_says("Years of **experience**?")
                next_step()

    elif st.session_state.step == 4:
            if not user_input.isdigit():
              st.error("Experience must be a number.")
            else:
              st.session_state.data["experience"] = int(user_input)
              bot_says("Desired **position(s)**?")
              next_step()

    elif st.session_state.step == 5:
          st.session_state.data["position"] = user_input
          bot_says("Current **location**?")
          next_step()

    elif st.session_state.step == 6:
        st.session_state.data["location"] = user_input
        name = st.session_state.data.get("name", "")
        experience = st.session_state.data.get("experience", "")

        bot_says(
            f"Great {name}! Which technologies are you most comfortable with? "
            "please list your tech stack (comma separated):"
        )
        next_step()

    elif st.session_state.step == 7:
        # Parse and store tech stack
        tech_stack = [tech.strip() for tech in user_input.split(",") if tech.strip()]
        st.session_state.data["tech_stack"] = tech_stack

        bot_says("Thanks! I’m generating some technical questions for you...")

        # Build candidate context
        candidate_context = f"""
    Candidate Name: {st.session_state.data.get("name")}
    Experience: {st.session_state.data.get("experience")} years
    Desired Role: {st.session_state.data.get("position")}
    Tech Stack: {", ".join(tech_stack)}
    """

        # Store prompt in session state (IMPORTANT)
        prompt = f"""
             {candidate_context}

    Based on the above candidate profile, generate 5 technical interview questions
    that are relevant to the candidate's experience level and role.
    Return only numbered questions.
    """

        # Mark that we are ready to show questions
        questions = get_llm_response(SYSTEM_PROMPT + "\n" + prompt)

    # Display ONLY technical questions
        st.markdown("## Technical Interview Questions")
        st.write(questions)
        st.stop()
if st.session_state.get("show_questions", False):
    st.markdown("## Technical Interview Questions")
    st.write(st.session_state.mock_questions)
    st.stop()
    