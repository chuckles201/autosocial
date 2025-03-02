# importing library
from playwright.sync_api import sync_playwright

# data-directory
data_dir_chrome = r"C:\Users\charl\AppData\Local\Google\Chrome\User Data Copy"
# creating chrome path
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


# posting function
def post_X(url='https://test.com'):
    with open("posting/tweet.txt","r") as file:
        tweet = file.read()

    tweet = f"{url}\n" + tweet
    # closes browser when done
    with sync_playwright() as p:
        # open our browser
        browser = p.chromium.launch_persistent_context(user_data_dir=data_dir_chrome,
                                                    executable_path=chrome_path,
                                                    headless=False)
        
        # getting on page
        page = browser.new_page()
        page.goto("https://x.com/")
        page.wait_for_selector('[data-testid="SideNav_NewTweet_Button"]', timeout=500)  # Waits up to 5s for the button
        page.click('[data-testid="SideNav_NewTweet_Button"]')
        
        page.wait_for_timeout(40)
        page.keyboard.type(tweet)
        page.click('button[data-testid="tweetButton"]')
        page.screenshot(path="posting/images/screenshot.png")
        

        
        
def post_HN(url='https://test.com'):
    with open("posting/tweet.txt","r") as file:
        # return first line... (title)
        tweet = file.read().splitlines()[0][:50]
        
        
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
        page.fill('input[name="title"]',tweet)
        
        # url
        page.wait_for_timeout(40)
        page.fill('input[name="url"]',url)
        
        # posting
        page.click('input[value="submit"]')
        
        # for testing
        page.wait_for_timeout(40)
        page.screenshot(path="posting/images/screenshot.png")
        
        
post_HN()