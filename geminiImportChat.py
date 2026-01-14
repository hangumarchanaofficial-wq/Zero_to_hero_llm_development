from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyDu3xFclyHTWUiq4Ju9iMgGUiwHhTgPVYw",
    base_url="https://openrouter.ai/api/v1",
)

response = client.chat.completions.create(
    model="google/gemini-1.5-pro",
    messages=[
        {"role": "system", "content": "You are a symbolic assistant."},
        {"role": "user", "content": "Interpret arc reactor in a dark way."},
    ],
)


print(response.choices[0].message.content)