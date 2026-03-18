from playwright.sync_api import sync_playwright

def scrape_youtube_comments_example(video_url):
    with sync_playwright() as p:
        # [비교 포인트 1: 브라우저 실행 속도]
        # Selenium의 WebDriver 구동 방식보다, WebSocket을 통해 
        # 브라우저와 직접 통신하는 Playwright의 실행 속도가 훨씬 빠릅니다.
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=True)

        print("1. 영상 페이지 접속 중...")
        # [비교 포인트 2: 똑똑한 페이지 로딩 대기]
        # Selenium: time.sleep()이나 묵시적 대기를 억지로 설정해야 함.
        # Playwright: 'networkidle' 옵션으로 네트워크 통신이 잠잠해질 때까지 스스로 판단해서 기다림.
        page.goto(video_url, wait_until="networkidle")
        
        print("2. 댓글 영역 활성화 중...")
        page.evaluate("window.scrollBy(0, 500)")
        page.wait_for_selector("ytd-comment-thread-renderer", state="visible")

        # [비교 포인트 3: Locator의 지연 평가]

        # Selenium (find_elements): 이 코드가 실행되는 즉시 현재 화면의 댓글 20개만 리스트로 고정함. 
        #                         나중에 스크롤하고 다시 접근하면 에러(StaleElementReferenceException) 발생!
        
        # Playwright (locator): 데이터를 지금 뽑지 않음! "나중에 데이터 달라고 하면 #content-text를 찾아라" 
        #                       라는 규칙만 만들어 두기 때문에, 스크롤 후에도 에러 없이 최신 상태를 반영함.
        comments_locator = page.locator("#content-text")
        
        print("3. 댓글 추가 로딩 스크롤 시작 (총 5회 진행)...")
        for i in range(5):
            current_count = comments_locator.count()
            
            page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight)")
            page.wait_for_timeout(1000) # 유튜브 서버가 스크롤을 인식할 1초의 물리적 쉼표
            
            try:
                # [비교 포인트 4: 완벽한 동적 대기 (Auto-waiting)]
                # Selenium: time.sleep(5)를 쓰면 1초 만에 로딩돼도 4초를 무조건 버려야 함.
                # Playwright: 5초를 한도로 잡되, 새 댓글이 감지되는 '그 순간' 즉시 다음 코드로 넘어감! (크롤링 시간 대폭 단축)
                page.wait_for_function(
                    f"() => document.querySelectorAll('#content-text').length > {current_count}",
                    timeout=5000 
                )
                print(f"  - 스크롤 {i+1}/5 완료 (현재 로드된 댓글: {comments_locator.count()}개)")
                
            except Exception:
                print(f"  - 스크롤 {i+1}/5: 지연 발생, 다음 스크롤 진행")

        final_count = comments_locator.count()
        print(f"\n🎉 최종 로드된 댓글 개수: {final_count}개")

        print("\n4. 상위 10개 댓글 내용 출력:")
        for i in range(min(10, final_count)):
            text = comments_locator.nth(i).inner_text().strip()
            print(f"[{i+1}] {text}\n")

        browser.close()

if __name__ == "__main__":
    url = "https://youtu.be/n8fdEYaDtfM?si=7Pj9FONzaTrQncKv"
    scrape_youtube_comments_example(url)