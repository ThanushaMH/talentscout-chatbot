import subprocess
import random

USE_MOCK = False      # set True only if LLaMA is unavailable
USE_LLAMA = True      # we are using LLaMA now


def get_llm_response(prompt):
    if USE_MOCK:
        return get_random_mock_questions()
    elif USE_LLAMA:
        return get_llama_response(prompt)


def get_llama_response(prompt):
    """
    Calls local LLaMA model via Ollama
    """
    try:
        result = subprocess.run(
            ["C:\\Users\\thanu\\AppData\\Local\\Programs\\Ollama\\ollama.exe", "run", "tinyllama"], 
            input=prompt,
            text=True,
            capture_output=True,
            timeout=180
        )
        print("OLLAMA STDOUT:", result.stdout)
        print("OLLAMA STDERR:", result.stderr)
        return result.stdout.strip()
    except Exception as e:
        return f"Error generating questions: {str(e)}"


# Fallback mock questions (still useful)
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
    ]
]


def get_random_mock_questions():
    questions = random.choice(MOCK_QUESTIONS_POOL)
    return "\n".join(questions)