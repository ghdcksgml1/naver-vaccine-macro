# 💉 네이버 톡톡을 이용한 네이버 백신 매크로

<img width="200" alt="스크린샷 2021-07-22 오후 3 50 11" src="https://user-images.githubusercontent.com/79779676/126601018-97629d4a-82a1-42f0-807e-19f8e18b96d1.png">


    결론 먼저 말씀드리면, 이 매크로로 백신을 신청하는 것은 불가능합니다.

    이유는 잔여백신이 생길 경우 알람이 네이버 알림 > 카카오톡 알림 > 네이버 톡톡 순이기 때문에 불가능.. ㅠㅠ

    실험 결과 네이버 톡톡은 네이버 알림 발생 후 10초 정도 뒤에 오는 것을 확인했습니다.
    
<br/><br/>

# 💉 필수 설치

### ![icons8-python-48](https://user-images.githubusercontent.com/79779676/126363111-57fdad9e-f8e6-4d4f-908d-2dc0dba9a606.png)Python 3.9 + Module ( selenium, bs4, tkinter )
### ![icons8-google-48](https://user-images.githubusercontent.com/79779676/126363753-5eded8a9-8dee-4b0f-9906-bfca4d24ac78.png) chormedriver

- 설치되어 있는 크롬의 버전과 설치할 webdriver의 버전이 일치해야 합니다. ( 오류의 원인 )

<img width="1192" alt="스크린샷 2021-07-21 오전 2 33 07" src="https://user-images.githubusercontent.com/79779676/126369549-8f36df56-9b23-4e6e-80a2-1162128bf9e1.png">

<br/>

### 다운로드 링크
* python : https://www.python.org/downloads/
* chrome driver : https://chromedriver.chromium.org/downloads

<br/><br/>
    
    
# 💉 사용 방법

1. python을 실행 시킨다.
2. webdriver파일 선택 후, 준비 클릭
3. 네이버 로그인 후 네이버 백신예약 1회인증
4. 네이버 톡톡으로 들어가 네이버 우리동네 백신알림 채팅창 들어가기

<img width="535" alt="스크린샷 2021-07-22 오후 3 53 00" src="https://user-images.githubusercontent.com/79779676/126600982-f1404918-d937-4828-8f84-d378c3b3bb81.png">

6. 시작 클릭 (pyhton 창에 시작 누른 후 몇초 지났는지 나옴)
7. 다시 시작하려면 다시 시작하거나, 리셋 버튼 클릭 (다시 시작할 경우 백신예약 인증 다시해야함)

<br/><br/>

# 💉 작동 원리

가장 마지막 알람이 왔던 시간을 웹 크롤링을 통해 저장해둡니다.

1초에 한번씩 웹을 크롤링하며 가장 마지막 알람의 시간을 가져오는데

이 값이 바뀌게 되면 ['지금 신청하기']() 버튼을 클릭합니다. (알람이 새로 옴)

새 창이 열리게 되면, 웹 드라이버로 다루고 있는 창을 바꿔주고, 동의합니다 버튼 클릭 후 백신 예약 클릭

<img width="200" alt="스크린샷 2021-07-22 오후 4 07 18" src="https://user-images.githubusercontent.com/79779676/126601643-eeb96e89-691b-4f43-91e9-5bc1ecbc999d.png">

<br/><br/>

# 💉 시도

제가 직접 2차례 시도를 해보았습니다.

결과는 2시도 0성공 2실패 서두에 말했다시피, 네이버알림 > 카카오톡 > 네이버톡톡 순으로 오기 때문에

네이버톡톡으로 바로 들어간다 쳐도 너무 느려요.. (네이버톡톡에서는 바로 반응합니다.)

사람들이 1초 만에 반응하기 때문에 10초 정도 늦게 들어가면 못한다고 보시면 됩니다.

아마 네이버 측에서 막은 것 같기두...

아무튼, 저는 그냥 순서가 오면 그때 맞으렵니다.....
