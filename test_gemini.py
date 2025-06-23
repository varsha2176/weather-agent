from langchain_community.chat_models.google_generative_ai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyBIU_8TuXWRQjhXJTU9sDZBHkIIBvHPQRQ")
response = llm.invoke("Tell me a joke.")
print(response)
