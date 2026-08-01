from groq import Groq
import os
import sys

API_KEY = os.getenv("gsk_your_key_here")
MODEL = "llama-3.1-8b-instant"
SYSTEM_PROMPT_PATH = "system_prompt.txt"

def load_system_prompt(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f"System prompt not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def create_client(api_key: str) -> Groq:
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Set it as an environment variable or pass it directly.")
    return Groq(api_key=api_key)

def chat(client: Groq, history: list, user_message: str) -> str:
    history.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model=MODEL,
        messages=history,
        temperature=0.6,
        max_completion_tokens=1024,
        top_p=0.9
    )

    assistant_reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply

def main():
    try:
        system_prompt = load_system_prompt(SYSTEM_PROMPT_PATH)
        client = create_client(API_KEY)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    history = [{"role": "system", "content": system_prompt}]

    print("=" * 60)
    print("Psychological Intake Assistant")
    print("Type 'exit' to quit")
    print("=" * 60)

    try:
        reply = chat(client, history, "Hello")
        print(f"\nAssistant: {reply}")
    except Exception as e:
        print(f"Failed to generate initial response: {e}")
        sys.exit(1)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("\nSession ended.")
            break

        if not user_input:
            continue

        try:
            reply = chat(client, history, user_input)
            print(f"\nAssistant: {reply}")
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()