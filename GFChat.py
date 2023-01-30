
import os
import openai

openai.api_key = "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"

context = "Chat between user and virtual girlfriend:\n"

# Loop indefinitely to continue the conversation
while True:
    # Read the user's message
    message = input(">?>?> ")
    if message == "stop": break
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=1024,
        temperature=0.5,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        # contextvars=context,
        # stop=["You:"]
    )

    text = response['choices'][0]['text']
    # Print the response
    print("gf:", text)
