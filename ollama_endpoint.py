import requests

model = "gemma3:4b"
headers = {
    "Authorization": "Bearer ollama",
    "Content-Type": "application/json"
}
print("HI there , this is gemma3:4b model")
while True:
    user_input = input("Enter your message: ")
    if user_input == "exit":
        break



    payload = {
        "model": model,
        "messages": [{"role": "user", "content": user_input}],
        "stream": False
    }

    url = "http://localhost:11434/v1/chat/completions"

    response = requests.post(url, headers=headers, json=payload)
    print(response.json()["choices"][0]["message"]["content"])