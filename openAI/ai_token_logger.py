from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        # Print AI response
        print("AI Response:", response.choices[0].message.content)

        # Print token usage
        print("---- Token Usage ----")
        print("Prompt tokens:", response.usage.prompt_tokens)
        print("Completion tokens:", response.usage.completion_tokens)
        print("Total tokens:", response.usage.total_tokens)
        print("---------------------")

    except Exception as e:
        print("Error:", e)

# Example call
ask_ai("Summarize the history of the Internet in 3 bullet points.")
