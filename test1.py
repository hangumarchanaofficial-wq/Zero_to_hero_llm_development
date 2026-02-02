import ollama

model="gemma3:4b"

messages = [
    {"role":"system", "content":"you are a helpful assistant. who assistant with scientific meaning? , and guess the scientific meaning words out of arc reactor  " },
    {"role": "user", "content": "give me all the possible dark meanings of arc reactor and it's made up words  "}
]
res = ollama.chat(model,messages=messages)
print(res.message.content)
