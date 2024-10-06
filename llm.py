import os
import google.generativeai as genai
import markdown2

genai.configure(api_key="AIzaSyAiSiLud9BOksq_vfiLtCZKHJGucGYf57A")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-002",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="You are space trivia chatbot, Your name is AstroBot.\nYou have to solve queries for the user in fun and interesting way.\nKeep the chat engaging for high user interaction. \n\nMake the answer a little concise & remove the unnecessary jargon.\nUse emoji in it\n",
)

chat_session = model.start_chat(history=[])

def chat_with_llm(user_input):
    response = chat_session.send_message(user_input)
    response = markdown_to_html(response.text)
    return response

def markdown_to_html(markdown_text):
    markdowner = markdown2.Markdown()
    html_text = markdowner.convert(markdown_text)
    return html_text

if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        response = chat_with_llm(user_input)
        print("AstroBot:", response)