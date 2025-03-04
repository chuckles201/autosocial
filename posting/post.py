# importing library
from playwright.sync_api import sync_playwright
import json

# data-directory
data_dir_chrome = r"C:\Users\charl\AppData\Local\Google\Chrome\User Data Copy"
# creating chrome path
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


# getting file/post
with open("posting/recources/tweet.txt","r",encoding='utf-8') as file:
        tweet = file.read()

# posting function
def post_X(url='https://test.com'):

    post = f"{url}\n" + tweet
    # closes browser when done
    with sync_playwright() as p:
        # open our browser
        browser = p.chromium.launch_persistent_context(user_data_dir=data_dir_chrome,
                                                    executable_path=chrome_path,
                                                    headless=False)
        
        # getting on page
        page = browser.new_page()
        page.goto("https://x.com/")
        
        # need to wait for visibility
        page.wait_for_selector('[aria-label="Post"]', state="visible",timeout=5000)  # Waits up to 5s for the button
        page.click('[aria-label="Post"]')
        
        page.wait_for_timeout(40)
        page.keyboard.type(post[:270])
        page.click('button[data-testid="tweetButton"]')
        page.screenshot(path="posting/images/Xscreenshot.png")
        

        
        
def post_HN(url='https://test.com'):

    title = tweet.splitlines()[0][:275]
        
    # closes browser when done
    with sync_playwright() as p:
        # open our browser
        browser = p.chromium.launch_persistent_context(user_data_dir=data_dir_chrome,
                                                    executable_path=chrome_path,
                                                    headless=False)
        
        # getting on page
        page = browser.new_page()
        page.goto("https://news.ycombinator.com/submit")
        page.wait_for_selector('input[name="title"]', timeout=500)  # Waits up to 5s for the button
        
        # title
        page.wait_for_timeout(40)
        page.fill('input[name="title"]',title[:80])
        
        # url
        page.wait_for_timeout(40)
        page.fill('input[name="url"]',url)
        
        # posting
        page.click('input[value="submit"]')
        
        # for testing
        page.wait_for_timeout(40)
        page.screenshot(path="posting/images/HNscreenshot.png")


def post_reddit(url="https://test.com",type="[D]"):
    # specify type so is saved
    title = type+tweet.splitlines()[0][:200]
    rest = f"{url}\nTLDR article:\n" + tweet[len(title):]
    # open our browser
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(user_data_dir=data_dir_chrome,
                                                    executable_path=chrome_path,
                                                    headless=False)
        
        # getting on page
        page = browser.new_page()
        page.goto("https://www.reddit.com/r/MachineLearning/submit/")
        
        # write
        page.wait_for_selector('textarea[name="title"]', timeout=5000)  # Waits up to 5s for input
        page.fill('textarea[name="title"]',title)
        page.wait_for_timeout(40)
        page.fill('[aria-label="Post body text field"]',rest)
        page.wait_for_timeout(40)
        
        
        # submit, screenshot 
        page.wait_for_selector('button[id="inner-post-submit-button"]', timeout=5000)  # Waits up to 5s for input
        page.click('button[id="inner-post-submit-button"]')
        page.wait_for_timeout(2000) # wait to post...
        page.screenshot(path="posting/images/redditScreenshot.png")

# function to type with shift-space
# make sure element already selected
def type_shiftEnter(page,post):
    for i in post[:1900].splitlines():
        # type line, indent!
        page.keyboard.type(i)
        page.keyboard.down("Shift")
        page.keyboard.press("Enter")
        page.keyboard.up("Shift")
    page.keyboard.press("Enter")

# posting function
def post_Discord(url='https://test.com',just_title=True):

    if just_title:
        post = tweet.splitlines()[0] + f"\n{url}"
    else:
        post = f"{url}\n" + tweet
        
    # closes browser when done
    with sync_playwright() as p:
        # open our browser
        def post_func(link):
            browser = p.chromium.launch_persistent_context(user_data_dir=data_dir_chrome,
                                                        executable_path=chrome_path,
                                                        headless=False)
            
            # getting on page
            page = browser.new_page()
            page.goto(link)
            
            # wait for load,write
            page.wait_for_selector('svg[class="icon__9293f"]', state="visible",timeout=5000)  # Waits up to 5s for the button
            type_shiftEnter(page,post)
            
            # proof
            page.wait_for_timeout(40)
            page.screenshot(path="posting/images/Discscreenshot.png")
            browser.close()
            
        # doing all parts
        with open("posting/recources/discord.json",'r') as file:
            data = json.load(file)
        
        for l in data['discord_servers']:
            post_func(l)

