import ollama
import requests
from bs4 import BeautifulSoup

model ="gemma3:4b"

system_Prompt = {
    "role": "system",
    "content": (
        "You are an assistant that analyzes the content of a website and provides a short summary, "
        "ignoring text that might be navigation related, and respond in markdown."
    )
}


def website_extractor(url:str , timeout: int=20) -> str:
    headers = {"User-Agent": "Mozilla/5.0 (compatible; website_extractor/1.0)"}
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    for tag_name in ["footer", "header", "nav", "aside"]:
        for tag in soup(tag_name):
            tag.decompose()

    return soup.get_text(strip=True)

user_prompt_prefix = (
    "Here are the content of a website,\n"
    "provide a short summary of this website in markdown,\n"
    "IF it includes news or announcements, then summarize these too.\n\n"

)
url = input("Enter the URL of the website: ")

messages = [
    system_Prompt,
    {"role":"user", "content":user_prompt_prefix + website_extractor(url)}
]
resp = ollama.chat(model,messages=messages)
print(resp.message.content)




