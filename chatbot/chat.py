import os 
from dotenv import load_dotenv 
from google import genai
import sys 


load_dotenv()

class ConversationalChatbot: 
    def __init__(self) -> None:
        # Load the gemini api 
        self.model = genai.Client(api_key=os.getenv("GEMINI_API")) 

    def chat(self, user_input: str) -> str:
        # Chatbot response generation 
        response = self.model.models.generate_content(
                                                model="gemini-2.0-flash",
                                                contents=user_input)
        return response.text 


if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
    load_dotenv()  
    chatbot = ConversationalChatbot() 
    print(chatbot.chat("Hello"))