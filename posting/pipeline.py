import post 
import claude_summ
import guinter
import playwright
import markdowndownload as markdowndownload
import time
import importlib

'''
In this file, we make use of the posting functions
and the LLM response ability to

1. Extract the article in a readable form for the LLM
2. Hava claude write a summary.
3. Post to platforms

'''

# summarizing and posting an article
def summarize_post(use_claude = True):
    
    # gather info, add/download article and instructions...
    url,additional_instructions,default_instructions,x_post,post_hn,post_reddit,post_Disc,length = guinter.guiApp()
    print(url,additional_instructions,default_instructions,x_post,post_hn,post_reddit,post_Disc,length)
    if markdowndownload.create_url_markdown(url) == 0:
        pass
    else:
        print("ERror, stopped program...")
        return "error"
    
    if (use_claude == True):
        with open("posting/recources/extra_instructions.txt",'w',encoding='utf-8') as file:
            file.write(f"{additional_instructions}")
        # getting summary, saving
        claude_summ.create_summary_title(max_len=length,default_instructions=default_instructions)

    # reload so we can acess new file!
    importlib.reload(post)
    # posting to socials
    if (x_post == True):
        post.post_X(url=url)
    if (post_hn == True):
        post.post_HN(url=url)
    if (post_Disc == True):
        post.post_Discord(url=url)
    if (post_reddit == True):
        post.post_reddit(url=url)
        
    
    

summarize_post()