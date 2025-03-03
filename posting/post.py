# importing library
from playwright.sync_api import sync_playwright

# data-directory
data_dir_chrome = r"C:\Users\charl\AppData\Local\Google\Chrome\User Data Copy"
# creating chrome path
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


# getting file/post
with open("posting/tweet.txt","r") as file:
        tweet = file.read()

# posting function
def post_X(url='https://test.com'):

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
        
        # need to wait for visibility
        page.wait_for_selector('[aria-label="Post"]', state="visible",timeout=5000)  # Waits up to 5s for the button
        page.click('[aria-label="Post"]')
        
        page.wait_for_timeout(40)
        page.keyboard.type(tweet[:270])
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
        page.goto("https://www.reddit.com/r/EJJohnsonMagic/submit/?type=TEXT")
        
        # write
        page.wait_for_selector('textarea[name="title"]', timeout=5000)  # Waits up to 5s for input
        page.fill('textarea[name="title"]',title)
        page.wait_for_timeout(40)
        page.fill('[aria-label="Post body text field"]',rest)
        page.wait_for_timeout(40)
        
        # add flair
        page.click('button[id="reddit-post-flair-button"]')
        page.wait_for_timeout(40)
        
        # submit, screenshot
        if page.locator("")
        page.wait_for_selector('button[id="inner-post-submit-button"]', timeout=5000)  # Waits up to 5s for input
        page.click('button[id="inner-post-submit-button"]')
        page.wait_for_timeout(2000) # wait to post...
        page.screenshot(path="posting/images/redditScreenshot.png")
        
        
        
        
post_reddit(url="https://www.drive.com.au/guides/electric-cars/")