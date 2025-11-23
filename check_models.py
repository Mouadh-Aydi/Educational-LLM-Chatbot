import google.generativeai as genai

# 1. SETUP YOUR KEY
api_key = "AIzaSyCq7j8gweb-M4UNswBlfUyBOIk4yeG0T4I" # <--- Put your AIzaSy... key here

genai.configure(api_key=api_key)

print("Checking available models...")
try:
    # 2. ASK GOOGLE WHAT IS AVAILABLE
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error: {e}")