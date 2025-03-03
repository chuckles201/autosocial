import post 
import claude_summ

'''
In this file, we make use of the posting functions
and the LLM response ability to

1. Manually add the article in article.txt
2. Hava claude write a summary.
3. Post to platforms

'''

# summarizing and posting an article
def summarize_post(url,use_claude = True):
    
    # potential additional instructions
    x_post = True # TODO: Call GUI
    post_hn = True
    
    if (use_claude == True):
        additional_instructions = str(input("Additional Instructions for Claude: "))
        with open("instructions.txt",'a') as file:
            file.write(f"\n{additional_instructions}")
        
        # getting summary, saving
        claude_summ.create_summary_title(max_len=200)


    # posting to socials
    if (x_post == True):
        post.post_X(url=url)
    if (post_hn == True):
        post.post_HN(url=url)
        
    
summarize_post(url="https://test.com",use_claude=True)