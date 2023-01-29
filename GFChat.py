import os
import openai

openai.api_key = "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"

prompt = "Hi, I'm your virtual girlfriend. What's on your mind?"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5
    # top_p=1.0,
    # frequency_penalty=0.5,
    # presence_penalty=0.0,
    # stop=["You:"]
)

# Loop indefinitely to continue the conversation
while True:
    # Read the user's message
    message = input(">?>?>?> ")
    if message == "stop": break
    # Use the ChatGPT API to generate a response to the user's message
    response = openai.Completion.create(
        engine="text-davinci-002", prompt=f"{prompt}\n{message}", max_tokens=1024, temperature=0.5)

    # Print the response
    print(response.text)
