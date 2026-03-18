#pick locator 활용
from playwright.sync_api import sync_playwright

play = sync_playwright().start()
browser = play.chromium.launch(headless=False,args=["--start-maximized"])
page = browser.new_page(no_viewport=True)

###--------------------------------------------------### browser와 page
page.goto("https://finance.naver.com/")
page.pause()

###--------------------------------------------------### url로 이동


###--------------------------------------------------### 국내증시, 시가총액 클릭 


###--------------------------------------------------### 시가총액 table에서 column name과 첫번째 데이터 추출 print  #page.locator("table",has_text="코스피") 도 가능


###--------------------------------------------------### tag_table,tag_header,tag_body로 정리 # all~은 리스트형식 반환


###--------------------------------------------------### 반복문으로 출력 
# import json
# dumped = json.dumps({"header" : tag_header, "body": tag_body},indent=2,ensure_ascii=False)
# with open("page_1.json","w",encoding="utf-8") as fp:
#     fp.write(dumped)
#     pass
###--------------------------------------------------### json출력