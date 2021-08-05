# 💉 네이버 백신 매크로

<img width="1100" alt="Screen Shot 2021-08-05 at 3 32 02 AM" src="https://user-images.githubusercontent.com/79779676/128235700-c63e37cc-7a2a-4da9-a5f1-a2358efd4145.png">

    기존 네이버 톡톡으로 들어가는 방식에서 네이버 모바일 진입을 통한 방식으로 바꾸었습니다.
    
    link 1: , link 2: , link 3: 에 들어가야 하는 곳은 병원의 코드인데
    
    병원의 코드는 아래와 같이 추출할 수 있습니다.
    
1. 내가 알림예약한 병원 네이버 지도로 들어가기

2. 병원 코드 추출

<img width="851" alt="스크린샷 2021-07-29 오전 10 12 13" src="https://user-images.githubusercontent.com/79779676/127416163-3d638294-539e-4cba-80df-a3925fae5eeb.png">


    
<br/><br/>

# 💉 필수 설치

### ![icons8-python-48](https://user-images.githubusercontent.com/79779676/126363111-57fdad9e-f8e6-4d4f-908d-2dc0dba9a606.png)Python 3.9 + Module ( selenium, bs4, tkinter, time )

    cd desktop
    cd naver-vaccine-macro
    pip install -r requirements.txt  or  pip3 install -r requirements.txt

### ![icons8-google-48](https://user-images.githubusercontent.com/79779676/126363753-5eded8a9-8dee-4b0f-9906-bfca4d24ac78.png) chormedriver

- 설치되어 있는 크롬의 버전과 설치할 webdriver의 버전이 일치해야 합니다. ( 오류의 원인 )

<img width="1192" alt="스크린샷 2021-07-21 오전 2 33 07" src="https://user-images.githubusercontent.com/79779676/126369549-8f36df56-9b23-4e6e-80a2-1162128bf9e1.png">

<br/>

### 다운로드 링크
* python : https://www.python.org/downloads/
* chrome driver : https://chromedriver.chromium.org/downloads

<br/><br/>
    
    
# 💉 사용 방법

    1. vaccinemacro.py 실행
    
    2. chromedriver.exe 선택
    
    3. link 1, link 2, link 3에 병원 코드 입력
    
    4. '준비' 누르면 화면이 뜸
    
    5. 네이버 로그인 후 잔여백신 휴대폰 인증하기
    
    6. '시작' 버튼 클릭
    
    7. 만약, 꺼졌다면 '리셋' 누르고 다시 '시작' 클릭

<br/><br/>

# 💉 작동 원리

    실시간 웹 크롤링을 통해 접종 예약하기 버튼이 활성화 되어 있는지를 확인합니다.
    
    활성화 되지 않았을 경우 다음 탭으로 넘어가서 다시 크롤링을 합니다.
    
    그렇게 첫번째 두번째 세번째 탭을 크롤링한 뒤 1.3초 대기하다가 다시 반복합니다.

<br/><br/>

https://user-images.githubusercontent.com/79779676/127417517-0fccfeb2-d0b8-48dd-a831-82c8dc503b7b.mp4

<br/><br/>

# 💉 시도


    인증을 시도할때 네이버 인증서로 인증하는 것이 아닌 휴대폰 인증으로 하게 되면 로그인이 오랫동안 유지되는 것을 발견했습니다.
    
    하지만, 로그인이 자꾸 풀리네요..
