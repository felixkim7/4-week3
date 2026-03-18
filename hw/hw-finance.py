
from playwright.sync_api import sync_playwright

play = sync_playwright().start()
browser = play.chromium.launch(headless=False,args=["--start-maximized"])
page = browser.new_page(no_viewport=True)

page.goto("https://finance.naver.com/")
page.pause()

##################################################
#######         코드를 작성해주세요           #######
##################################################