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

st.set_page_config(page_title="TalentScout Hiring Assistant")

st.title("TalentScout Hiring Assistant")

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.data = {}
    st.session_state.show_questions = False

def next_step():
    st.session_state.step += 1



exit_words = ["exit", "quit", "bye"]

st.text_input(
    "You:",
    key="input",
    on_change=handle_input
)

user_input = st.session_state.get("last_input", "")
if user_input:
    if user_input.lower() in exit_words:
        st.success("Thank you for your time! Our team will contact you soon.")
        st.stop()

    if st.session_state.step == 0:
        st.write("Hello! I'm TalentScout. I will assist with your initial screening. Let's begin!!")
        st.write("What is your **full name**?")
        st.session_state.step += 1

    elif st.session_state.step == 1:
        st.session_state.data["name"] = user_input
        st.write("Enter your **email address**:")
        next_step()

    elif st.session_state.step == 2:
        if not is_valid_email(user_input):
         st.error("Please enter a valid email address.")
        else:
            st.session_state.data["email"] = user_input
            st.write("Enter your **phone number**:")
            next_step()

    elif st.session_state.step == 3:
            if not is_valid_phone(user_input):
                st.error("Phone number must be 10 digits.")
            else:
                st.session_state.data["phone"] = user_input
                st.write("Years of **experience**?")
                next_step()

    elif st.session_state.step == 4:
            if not user_input.isdigit():
              st.error("Experience must be a number.")
            else:
              st.session_state.data["experience"] = int(user_input)
              st.write("Desired **position(s)**?")
              next_step()

    elif st.session_state.step == 5:
        st.session_state.data["position"] = user_input
        st.write("Current **location**?")
        next_step()

    elif st.session_state.step == 6:
        st.session_state.data["location"] = user_input
        st.write("List your **tech stack** (comma separated):")
        next_step()

    elif st.session_state.step == 7:
        tech_stack = [tech.strip() for tech in user_input.split(",") if tech.strip()]
        st.session_state.data["tech_stack"] = tech_stack

        st.write("### Technical Questions:")

        if "mock_questions" not in st.session_state:
            st.session_state.mock_questions = get_llm_response(SYSTEM_PROMPT)

        questions = st.session_state.mock_questions


        st.write(questions)

        st.success("Thank you! Our team will review your profile.")
        st.stop()

if st.session_state.get("show_questions", False):
    st.markdown("## Technical Interview Questions")
    st.write(st.session_state.mock_questions)
    st.stop()