# hateslop 4기 실습 · Week 3

hateslop 4기 실습 3주차 (Crawling) 폴더입니다. 이번 주차에서는 정적 크롤링(BeautifulSoup)과 동적 크롤링(Selenium, Playwright)을 학습합니다.

## 개요

- 실습용 저장소 (Static Crawling, Dynamic Crawling, API 연동 등)
- `static-crawling/`: BeautifulSoup를 이용한 정적 크롤링 예제
- `dynamic-crawling/`: Selenium 및 Playwright를 이용한 동적 크롤링 예제
- `hw/`: 주차별 과제 제출 및 안내
- `api-practice/`: GDELT API 및 Newspaper3k를 이용한 추가 과제

## 저장소 구조

```
4-crawling_practice/
├── README.md           # 프로젝트 개요
├── requirements.txt    # Python 의존성
├── static-crawling/    # 정적 크롤링 실습 (ipynb)
│   └── jisigin.ipynb
├── dynamic-crawling/   # 동적 크롤링 실습 (ipynb)
│   ├── cat.ipynb
│   └── finance_playwright.py
├── hw/                 # 주차별 과제 (py 변환 제출)
│   └── [본인 폴더]/      # 개인 폴더 생성 (예: name_folder)
│       ├── hw-aladin.py  # [과제1] 알라딘 도서 페이지 크롤링
│       ├── hw-yanolja.py # [과제2] 야놀자 리뷰 페이지 크롤링
│       ├── hw-finance.py # [과제3] 네이버 증권 페이지 크롤링
│       └── hw-finance_result.png # [과제3 결과물] 캡처본,텍스트 등
├── api-practice/       # [추가과제] API 활용 과제 (선택)
│   ├── newpaper.ipynb
│   └── newpaper.py
└── example_code/       # 기타 예제 코드
    ├── capture_kospi.py
    └── scrape_youtube_comments.py
```

## 시작하기

### 환경 설정

1. **가상환경 생성 및 활성화**  
   `python -m venv .venv` 후 `.venv/bin/activate` (Windows는 `.venv\Scripts\activate`)

2. **의존성 설치**  
   `pip install -r requirements.txt`

3. **브라우저 드라이버 설정 (Playwright 사용 시)**  
   `playwright install`

## .ipynb → .py 변환 가이드 (과제 제출용)

GitHub에서 코드 리뷰를 원활하게 진행하기 위해, **`hw/` 폴더에 제출하는 과제 결과물**은 반드시 `.py` 파일로 변환하여 제출해 주세요.

### 변환 방법 (Terminal/Command Prompt)

1. 해당 폴더로 이동합니다.
2. 다음 명령어를 실행하여 변환합니다.
   ```bash
   python -m jupyter nbconvert --to script [파일명].ipynb
   ```
   *예시: `python -m jupyter nbconvert --to script hw-aladin.ipynb`*

## 과제 (Assignment)

### 1. 정적 크롤링: 알라딘 도서 페이지 크롤링 ([hw-aladin.ipynb](./hw/hw-aladin.ipynb))
- `requests`와 `BeautifulSoup`를 사용하여 베스트셀러 도서 데이터를 파싱하고 저장합니다.

### 2. 동적 크롤링: 야놀자 리뷰 페이지 크롤링 ([hw-yanolja.ipynb](./hw/hw-yanolja.ipynb))
- `Selenium`을 사용하여 동적으로 로드되는 호텔 리뷰 데이터를 수집합니다.

### 3. 동적 크롤링 2: 네이버 증권 페이지 크롤링 ([hw-finance.py](./hw/hw-finance.py))
- `Playwright`를 활용하여 네이버 증권 데이터를 추출합니다. 결과물은 캡처(`.png`, `.jpg`) 또는 텍스트 파일로 함께 제출해 주세요.

### 추가 과제 (선택): 뉴스 데이터 추출 ([newpaper.ipynb](./api-practice/newpaper.ipynb))
- `GDELT API`와 `Newspaper3k` 라이브러리를 사용해 뉴스 본문을 추출합니다.

## 제출 방법 및 규칙

1. **브랜치 및 폴더 생성**: 자신의 아이디로 브랜치 생성 후, `hw/` 폴더 내에 **개인 폴더**를 생성합니다.
   ```bash
   git checkout -b "your-branch-name"
   mkdir hw/"your-folder-name"
   ```
2. **작업 및 파일 변환**: 과제 작업물(`.ipynb`)은 반드시 `.py` 파일로 변환하여 개인 폴더에 담습니다.
3. **커밋 및 푸시**: 변경 사항을 추가하고 오리진에 푸시합니다.
   ```bash
   git add .
   git commit -m "[feat] ~~~~"
   git push origin "your-branch-name"
   ```
4. **Pull Request (PR)**: `main` 브랜치로 PR을 날려주세요.
   - PR 제목 예시: `week3_이름`

### 커밋 컨벤션
- `feat`: 새로운 기능 추가
- `fix`: 버그 수정
- `docs`: 문서 수정
- `style`: 코드 포맷팅 등
- `refactor`: 코드 리팩토링
- `chore`: 패키지 매니저 수정 등
