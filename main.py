from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("🤖 R F Bot is online! Type something...")

while True:
    user = input("You: ")
    if user.lower() in ["quit", "exit", "bye"]:
        print("R F Bot: Bye for now 👋")
        break

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are R F Bot, a friendly and smart AI assistant created by Rex."},
                {"role": "user", "content": user}
            ]
        )
        print("R F Bot:", response.choices[0].message.content)

    except Exception as e:
        print("⚠️ Error:", e)