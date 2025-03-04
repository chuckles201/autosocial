# autosocial
Automatically posts to all desired socials, finetuned LLM writes appealing/good titles and descriptions for each platform.

![cycle](cycle.png)

GUI:
![gui](posting/images/exampleGUI.png)

Watch video:

[![Watch the video](https://img.youtube.com/vi/pg5ajHkHW30/0.jpg)](https://www.youtube.com/watch?v=pg5ajHkHW30)

> [!Note]
I will probably not be using this as I post things in the future- although it was a cool/fun project! Personally, I beleive that posts should be made with care and intention- although this could be a glimpse into how future things will be done online.


# Goals
I want to create an application that takes a blog post you wrote, writes an appealing, but not over-the-top summary, and then shares this on various techical 'social media' websites.

The platforms it posts to:
- Hackernews
- Reddit
- X
- Discord (multiple servers)

--> For future
- Youtube (shorts,post) 
- Instagram (shorts,post)
- Medium/Other (re-upload?)

in the future, potentially we could use a video generation model to take our article and use a model to create a script, and video based on the article that is short and appealing, and serves to get the watcher interested in the article/share its true content.

Eventually, also I'd like it to automatically gather metrics.

# Overview

The code is in [posting](posting/), and is seperated in the following way:
- [post.py](posting/post.py): post a given URL and content to each social using playwright to automate browser actions
-[claude_summ.py](posting/claude_summ.py): Sends API call to Sonnet 3.7 and summarizes the website; takes [instructions.txt](posting/recources/instructions.txt) and [extra_instructions.txt](posting/recources/extra_instructions.txt) and modifies the tweet file for post.py to acess
- [guinter.py](posting/guinter.py): code for the gui that takes information about where to post/extra instructions to add
- [markdowndownload.py](posting/markdowndownload.py) takes the url, downloads the raw html, uses html2text (awesome) to convert html to markdown so an LLM can read it
- [pipeline.py](posting/pipeline.py) puts it all together: settings w/ GUI, extract w/html2text, summarize with claude, post with playwright!



## Conclusion: Working with AI like future

Write the conclusion about how you think AI will revoultionize communication, from governments/poltics, to reaching out to people. Will social and speaking abilities be rendered irrelevant?