import os
from playwright.sync_api import sync_playwright

def capture_element_screenshot():
    # 캡처 이미지를 저장할 폴더 이름 설정
    save_folder = "kospi_screenshots"
    
    # 폴더가 존재하지 않으면 새로 생성합니다.
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
        print(f"'{save_folder}' 폴더를 새로 생성했습니다.")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=True)

        print("1. 네이버 금융 메인 페이지 접속")
        page.goto("https://finance.naver.com/")

        # 캡처하고 싶은 특정 영역의 Locator를 지정 (ex: 현재 코스피)
        target_element = page.locator("div.kospi_area.group_quot.quot_opn")

        # 요소가 화면에 보일 때까지 대기 (Playwright의 장점)
        target_element.wait_for(state="visible")

        print("2. 특정 요소만 캡처하여 저장 중...")
        
        # 폴더 경로와 파일명을 합쳐서 최종 저장 경로를 만듭니다 (예: kospi_screenshots/kospi.png)
        file_path = os.path.join(save_folder, "kospi.png")
        
        # 요소 영역만 정확히 잘라서 이미지 파일로 저장
        target_element.screenshot(path=file_path)
        
        print(f"✅ '{file_path}' 위치에 캡처 저장 완료!")

        browser.close()

if __name__ == "__main__":
    capture_element_screenshot()