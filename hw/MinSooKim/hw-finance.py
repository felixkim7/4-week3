
from playwright.sync_api import sync_playwright

play = sync_playwright().start()
browser = play.chromium.launch(headless=False,args=["--start-maximized"])
page = browser.new_page(no_viewport=True)

page.goto("https://finance.naver.com/")
page.pause()

##################################################
#######         코드를 작성해주세요           #######
##################################################


# 해외증시 클릭
page.get_by_role("link", name="해외증시").click()


# 해외 주요지수 table 선택
table = page.locator("table", has_text="해외 주요지수")

# column name 추출
columns = table.locator("thead th").all_inner_texts()

# 첫 번째 데이터 행 추출
first_row = table.locator("thead tr").nth(1)
first_data = first_row.locator("td").all_inner_texts()

print("컬럼명:", columns)
print("첫 번째 데이터:", first_data)


# 테이블 정리
tag_table = table
tag_header = tag_table.locator("thead th").all_inner_texts()


all_rows = tag_table.locator("thead tr").all()
rows = all_rows[1:]

tag_body = []
for row in rows:
    row_data = row.locator("td").all_inner_texts()
    tag_body.append(row_data)



# 반복문으로 출력
print("\n[헤더]")
for h in tag_header:
    print(h)

print("\n[바디]")
for row in tag_body:
    print(row)



# json 출력
import json

dumped = json.dumps(
    {"header": tag_header, "body": tag_body},
    indent=2,
    ensure_ascii=False
)
with open("page_2.json", "w", encoding="utf-8") as fp:
    fp.write(dumped)



browser.close()

play.stop()
