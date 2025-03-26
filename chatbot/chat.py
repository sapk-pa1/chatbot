import os 
from dotenv import load_dotenv 
from google import genai
import sys 
from prompts.generation_prompt import chatbot_prompt 
from database.chromedb import ChromaStorage 

load_dotenv()

class ConversationalChatbot: 
    def __init__(self) -> None:
        # Load the gemini api 
        self.model = genai.Client(api_key=os.getenv("GEMINI_API"))
        self.vector_database = ChromaStorage() 
         


    def chat(self, user_input: str, history= [] ) -> str:
        prompt = chatbot_prompt.format(user_input=user_input, history= history)
        # Chatbot response generation 
        response = self.model.models.generate_content(
                                                model="gemini-2.0-flash",
                                                contents=prompt, 
                                                )
        return response.text 


if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
    load_dotenv()  
    chatbot = ConversationalChatbot() 
    print(chatbot.chat("Hello"))