import os
import anthropic

# saved in environement variable
api_pass = os.environ.get("anthropic_api_key")


def create_summary_title(max_len = 150):
    with open("posting/instructions.txt", "r") as file:
        instructions = file.read()
        
    with open("posting/article.txt", "r") as file:
        article = file.read()

    client = anthropic.Anthropic(
        api_key=api_pass
    )

    message = client.messages.create(
        # model-type
        model="claude-3-7-sonnet-20250219",
        # system rules
        system= instructions,
        # messages received
        messages=[
            {"role":"user",
            "content":article}
        ],
        max_tokens=max_len
        
    )

    msg = message.content[0].text
    token_ctO = message.usage.output_tokens
    token_ctI = message.usage.input_tokens
    cost = token_ctI * 3 * (10**-6) +  token_ctO * 15 * (10**-6) 
    
    with open('posting/tweet.txt','w') as tweet:
        tweet.write(msg)
        
    print("Tweeted, length of: ", token_ctO, " tokens")
    print("Cost of: $",cost)


create_summary_title()