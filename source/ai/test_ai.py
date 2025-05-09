from google import genai

client = genai.Client(api_key="AIzaSyBnUUsk6pBhrVeVGfVkiv3uf76nf0x2DOQ")

response = client.models.generate_content(model="gemini-2.0-flash", contents="Olá google.")

print(response.text)