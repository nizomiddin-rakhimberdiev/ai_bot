from google import genai

client = genai.Client(api_key="AIzaSyDpZNMY3YFLf78N8tq-6c29DRIypXk6_6A")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Men kechalari yaxshi uxlay olmayapman. men kechasi mazza qilib uxlashim uchun nima maslahat berasiz?"
)
print(response.text)