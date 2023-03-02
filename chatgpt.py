import os
import openai

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = ""

conversation = ""

while True:
    conversation = input("==> ")
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": conversation},
    ]
    )
    print(response['choices'][0]['message']['content'])
