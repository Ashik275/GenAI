from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import init_chat_model

# model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
model = init_chat_model("groq:openai/gpt-oss-120b",temperature=0)

response = model.invoke("What is laravel?")

print(response.content);
