import os
import random
from dotenv import load_dotenv

load_dotenv()

USE_MOCK = True  # Set False when real API is available

MOCK_QUESTIONS_POOL = [
    [
        "1. Explain the basic concepts of this technology.",
        "2. What are its real-world use cases?",
        "3. How does it differ from similar technologies?",
        "4. What are common mistakes beginners make?",
        "5. How would you optimize performance?"
    ],
    [
        "1. What problem does this technology solve?",
        "2. Explain its core architecture.",
        "3. How do you handle errors and debugging?",
        "4. What security concerns should be considered?",
        "5. Describe a real project where you used it."
    ],
    [
        "1. Explain basic to advanced concepts.",
        "2. How does this technology scale?",
        "3. What are its limitations?",
        "4. How do you test applications built with it?",
        "5. How do you deploy it in production?"
    ]
]

def get_llm_response(prompt):
    if USE_MOCK:
        return get_random_mock_questions()
    else:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )
        return response.choices[0].message.content

def get_random_mock_questions():
    questions = random.choice(MOCK_QUESTIONS_POOL)
    return "\n".join(questions)