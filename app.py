import gradio as gr
from chatbot.chat import ConversationalChatbot

# Initialize chatbot
bot = ConversationalChatbot()

def chat_function(user_input, history) -> str:
    response = bot.chat(user_input) 
    return response


# Gradio Chat Interface
chat_interface = gr.ChatInterface(
    fn=chat_function,
    textbox=gr.Textbox(placeholder="Type your message...", label="User Input"),
    title="XChat",
    description="A Conversational Chatbot",
    examples=["Hello", "How are you?", "What can you do?"],
)

# Run the Gradio app
if __name__ == "__main__":
    chat_interface.launch()