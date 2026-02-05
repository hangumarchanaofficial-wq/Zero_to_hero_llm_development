import google.generativeai as genai

# Set your key
genai.configure(api_key="AIzaSyCF052Nbe1pnWb259IZJsKBMGS4aQ3GlJM")

# Initialize the model
model = genai.GenerativeModel('gemini-2.5-flash')

# Generate a response
response = model.generate_content("Explain how a URL summarizer works.")
print(response.text)