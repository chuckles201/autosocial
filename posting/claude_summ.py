import os
import anthropic

# saved in environement variable
api_pass = os.environ.get("anthropic_api_key")


def create_summary_title(max_len = 150,default_instructions=True):
    print("Claude is Summarizing...")
    # if we want default instructions
    if default_instructions:
        with open("posting/recources/instructions.txt", "r",encoding='utf-8') as file:
            instructions = file.read()
    else:
        instructions = ""
    
    with open("posting/recources/extra_instructions.txt", "r",encoding='utf-8') as file:
        instructions_extra = file.read()
    
    instructions = instructions + "\n" + instructions_extra
    
    print("Instructions:\n",instructions)
        
    with open("posting/recources/article.txt", "r",encoding='utf-8') as file:
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
    
    with open('posting/recources/tweet.txt','w') as tweet:
        tweet.write(msg)
        
    print("Summarized, length of: ", token_ctO, " tokens")
    print("Cost of: $",cost)


