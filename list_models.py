# list_models.py
import google.generativeai as genai

genai.configure(api_key="AIzaSyBIU_8TuXWRQjhXJTU9sDZBHkIIBvHPQRQ")

for model in genai.list_models():
    print(model.name)
