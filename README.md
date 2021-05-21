# Section3-Solo-Project

블로그 주소 : https://github.com/codestates/ds-blog/issues/266

웹 어플리케이션 주소 : https://geunhoo-twit.herokuapp.com/


<p align="center">
<img width="400" height="400" src="https://user-images.githubusercontent.com/61172021/101047939-9637c980-35c5-11eb-99d5-9d73145f6680.png">
</p>

# Intro

본 프로젝트는 다음과 같은 작업을 포함합니다. 

1. Flask(웹 프레임워크)와 파이썬을 사용한 웹 어플리케이션 제작. 
2. 트위터 API 를 사용해서 불러온 데이터를 리모트 데이터 베이스에 저장하고 조작 (Create, Read, Update, Delete)
3. 리모트 데이터베이스에 저장된 데이터를 사용한 간단한 머신러닝을 수행. 

이번 프로젝트는 API, 파이썬코드, 리모트 데이터베이스, html 모두를 동시에 이해하고 그것들을 넘나드는 라이브러리와 패키지를 이해해야 합니다. Flask, SQLAlchemy, Tweepy 등 각자 이 프로젝트에서 큰 역할을 하는 것들이고 순서대로 의미가 있으니 아래에서 자세히 다루겠습니다. 

# 패키지와 라이브러리

1. Flask 

Flask 는 Python의 마이크로 웹 프레임워크입니다. 여기서 웹 프레임워크란 웹 서비스 개발을 위한 하나의 뼈대 역할이라고 보시면 됩니다. Flask 같은 웹 프레임워크를 사용하는 가능 큰 이유는 웹 서비스 개발을 쉽고 빠르게 하기 위해서 입니다. 특히, Flask 와 관련된 확장 기능들이 많기 때문에 API 서버를 만들기에 매우 편리합니다. 

2. SQLAlchemy

Flask 의 SQLAlchemy 는 ORM (Object Relational Mapper) 의 한 종류입니다. 데이터베이스와 상호작용할 때에 SQL 쿼리문을 사용하기도 하지만, SQLAlchemy 는 데이터베이스와 상호작용하는 것을 조금 더 친숙한 객체 형식으로 접근 가능하게 해주고, 코드 가독성이 좋다는 장점을 가지고 있습니다. 반면에, SQLAlchemy 로 복잡한 쿼리를 작성하는 것은 난이도가 높습니다.

3. Tweepy 

Tweepy 는 파이썬에서 트위터 API 를 손쉽게 사용할 수 있도록 해주는 패키지입니다. 트위터 API 를 사용해 직접 크롤링을 하는 것보다 Tweepy 를 사용하는 것이 훨씬 간단하고 빠릅니다.

> * 쉽게말해, 다음과 같이 이해하시면 되겠습니다!
> 
> Flask = 웹 어플을 만드는 뼈대
>
> SQLAlchemy = 앱과 데이터베이스를 연결시켜줌
>
> Tweepy = 파이썬에서 트위터 API 를 사용하게 해줌
>
> => 트위터 API 로부터 데이터를 받아오는것은 Tweepy, 그 데이터를 데이터 베이스에 저장하게 해주는 것은 SQLAlchemy, 이 모든 것을 앱이라는 형태로 가능하게 해주는 것은 Flask.

# 앱 설명

<p align="center">
<img width="1163" alt="스크린샷 2020-12-06 오전 4 29 40" src="https://user-images.githubusercontent.com/61172021/101261560-abeeef80-377b-11eb-9975-dd80a58281ec.png">
</p>

제가 만든 앱은 서로 다른 기능을 하는 총 9개의 페이지로 구성되어 있습니다.  

1. Home 페이지 : 웹 페이지를 열면 가장 처음보는 화면입니다. User 테이블의 전체 쿼리 결과도 보여지는 역할을 합니다. (User 테이블이 비어있다면 특별한 것은 안보입니다.)

2. Add 페이지 : 사용자가 트위터 유저의 'Screen Name' 을 입력하면, 트위터 API 를 사용해 불러온 그 유저의 정보 (ID, Username, Full Name, Location) 는 User 테이블에 저장되고, 그 유저가 게시한 트윗들의 기록 (ID, Text, User ID) 은 Tweet 테이블에 저장됩니다. 그것과 동시에 User 테이블의 전체 쿼리 결과를 보여줍니다.

3. Get 페이지 : 사용자가 이미 저장했던 트위터 유저의 'Screen Name' 을 입력하면, 그 유저의 트윗기록들을 Tweet 테이블로부터 불러와 보여 줍니다.

4. Delete 페이지 : 사용자가 이미 저장한 트위터 유저의 'Screen Name' 을 입력하면, Add 페이지에서 저장했던 그 유저의 데이터 모두를 User, Tweet 테이블에서 삭제시킵니다.

5. Update 페이지 : User 테이블에 저장한 트위터 유저의 'Full Name' 을 바꿀 수 있습니다. 

6. Compare 페이지 : 입력된 2명의 유저중 누가 더 특정 트윗을 높은 확률로 게시할 것인지 예측해줍니다. 

7. Map 페이지 : 사용자가 이미 저장한 트위터 유저의 'Screen Name' 을 입력하면, 그 유저의 계정 활동 위치를 구글맵에 보여줍니다. 

8. Trend (Show) 페이지 : 나라이름을 입력하면 그 나라의 실시간 트랜딩 토픽들을 10개 보여줍니다.

9. Trend (Delete) 페이지 : 나라이름을 입력하면 그 나라의 실시간 트랜딩 토픽들을 저장한 기록을 Trend 테이블에서 삭제시켜 줍니다.

# 파일 구성

아래는 웹 어플리케이션을 작동하도록 해주는 파일들의 구성입니다. 파일들은 각각 역할이있고, 서로 복잡하게 연결되어있으며, 많은 라이브러리, 패키지, 모듈 들을 사용합니다. 그래서 조금이나마 덜 헷갈리고자 파일들의 구조를 그려봤습니다!

<p align="center">
<img width="800" height="550" src="https://user-images.githubusercontent.com/61172021/101071384-e3289980-35df-11eb-8cf6-55144f818ac4.png">
</p>

# 작업 순서와 파일들의 역할

### 1. _ _ init _ _ .py 파일 생성 

( 1 ) create_app() 함수 안에 플라스크 어플리케이션 객체를 생성후 데이터베이스와 연결하고, 블루프린트들을 설정합니다 (블루프린트로 구현된 그룹 : routes 폴더안에 있는 파일들). 
( 2 ) 그리고 if _ _ name _ _ == "_ _ main _ _": 부분을 통해 create_app() 함수를 실행하고, app.run() 을 통해 앱을 실행합니다.

### 2. models.py 파일 생성 : 

SQLAlchemy 를 사용해 데이터베이스에 테이블들을 만드는 클래스를 생성합니다. 그리고 테이블간의 관계도 외래키, relationship 함수를 사용해 설정합니다. 


### 3. 데이터베이스와 연결시키기

이렇게 플라스크 앱과 테이블이 준비가 되었다면 아래 코드를 차례대로 실행합니다.
```
FLASK_APP=twit_app flask db init
```
```
FLASK_APP=twit_app flask db migrate
```
```
FLASK_APP=twit_app flask db upgrade
```
위 코드를 차례대로 실행하여 설정한 데이터 베이스를 생성하고 연결하는 작업을 해줍니다. 그러면 위 그림의 2번째 레벨에 있는 'migrations' 이라는 폴더가 생기고, 리모트 데이터 베이스에 코드로 작성한대로 테이블들이 생깁니다. (sqlite3 를 사용 할 시 설정한 경로에 파일이 생깁니다)

### 4. routes 폴더의 파일들 templates 폴더의 파일들 생성 : 

* main_routes.py = 가장 먼저 보이는 index.html 에 User 테이블의 정보를 전달하여 보여지게 합니다. 

* add_routes.py = add.html 로부터 (POST 방식으로 입력된) 트위터 유저의 username 을 전달받습니다. 그리고 그 유저의 정보와 트윗기록들을 User 테이블과 Tweet 테이블에 데이터를 저장합니다.

* get_routes.py = get.html 로부터 트위터 유저의 username 을 전달받습니다. 그 후, Tweet 테이블에 저장된 데이터중 해당 username 과 일치하는 레코드들을 쿼리하여 get.html 에 전달하고 보여지도록 합니다. (해당 유저가 게시한 트윗들을 보여줌)

* delete_routes.py = delete.html 로부터 트위터 유저의 username 을 전달받아 User 테이블과 Tweet 테이블에서 해당 유저의 레코드를 삭제합니다.

* update_routes.py = update.html 로부터 현재 full_name 과 새롭게 바꿀 full_name 을 전달받아서 User 테이블에있는 레코드를 업데이트 시켜줍니다.

* compare_routes.py = compare.html 로부터 2명의 유저와 예측하고싶은 문장(트윗)을 전달받습니다. 그리고, 그 유저들의 트윗 경향을 바탕으로 로지스틱회귀모델을 학습시키고, 입력된 문장(트윗)을 어느 유저가 더 높은 확률로 게시할 것인지 예측합니다.

* map_routes.py = map.html 로부터 트위터 유저의 username 을 전달받고, 그 유저의 location 값을 '위도'와 '경도'로 바꾸고 그것들을 다시 map.html 로 전달하여 Google 지도 API 를 사용해 구현한 지도에 나타나도록 합니다.

* trend_routes.py = trend.html 로부터 나라 이름을 전달받고, 그 나라 이름을 woeid (Where On Earth ID) 로 바꾸고 그 나라에서 화제가 되고있는 토픽들을 10개 찾은 후 Trend 테이블에 저장하고 보여줍니다.

* trend_delete_routes.py = trend_delete.html 로부터 나라이름을 전달받고, Trend 테이블에 저장된 해당 나라의 트랜딩 토픽들을 삭제합니다.


### 5. 코딩 작업이 끝났다면, FLASK_APP=twit_app flask run 을 실행하여 로컬에서 기능들을 테스트 합니다.

<img width="1595" alt="스크린샷 2020-12-04 오전 6 03 52" src="https://user-images.githubusercontent.com/61172021/101088135-8c7a8a00-35f6-11eb-98df-0b6f9b9bbc30.png">

### 6. 배포 준비

에러들을 모두 해결하고, 원하는대로 기능들이 작동한다면 이제 Heroku 를 통해 배포를 할 차례입니다. 그 전에, 이 어플이 어떤 언어를 사용하는지, 어떤 프로세스들을 실행하는지에 대한 부분을 Heroku 가 알 수 있도록 설정해줘야 합니다. 

* requirements.txt 파일 생성 : Heroku 가 요구하는 파이썬 파일은 requirements.txt, setup.py, Pipfile 입니다. 이 중 하나라도 있으면 Heroku 는 파이썬을 인지합니다. 그래서 저는 pip freeze > requirements.txt 를 실행해서 파이썬 패키지들의 목록을 저장했습니다. (위 '파일 구조 그림'에서 2번째 레벨에 위치)

* Procfile 생성 : Heroku 앱에서 웹 어플리케이션을 실행하라는 명령어를 설정합니다. Heroku 는 해당 파일을 읽고 어떤 프로세스들이 있는지 파악합니다. 그리고, 파이썬의 flask 를 웹 서버로 돌리기 위해서는 gunicorn 이라는 추가 패키지가 필요하니, 해당 패키지를 설치해준 후 requirements.txt 파일을 다시 업데이트 해주고, Procfile 파일에 web 프로세스를 다음과 같이 명시합니다 => web: gunicorn 'twit_app:create_app()'


### 7. Heroku 를 통해 웹 어플리케이션 배포하기

    * brew tap heroku/brew && brew install heroku 를 실행하여 Heroku CLI 를 설치합니다.
    * 설치 후 Heroku 에 로그인합니다. 
    * Heroku 어플을 만듭니다.
    * 깃 리모트 주소에 heroku 주소를 추가합니다.
    * git push heroku master:main 을 실행하여 배포를 마칩니다.

<img width="1582" alt="스크린샷 2020-12-04 오전 6 47 23" src="https://user-images.githubusercontent.com/61172021/101092313-d1a1ba80-35fc-11eb-9c5d-0f4ed3a69480.png">


# 마치며...

트위터 API 앱에 몇가지 기능을 더 만들어 봤습니다. 제가 집중한 기능은 유저의 location 에 관한 것이었는데요, 그 중 하나는 유저의 location 을 위도, 경도로 바꾸고 그것을 구글 지도에 나타내는 것이었습니다. 이것은 구글 지도 API 의 도움을 받아 어느정도 성공적으로 만든 것 같습니다. 두번째 기능은 맘처럼 되지 않았습니다. 저는 유저의 위치를 woeid (Where On Earth ID) 로 바꾸고 그 값으로 유저의 위치에서 화제가 되고있는 트랜딩 토픽들을 불러와 Trend 테이블에 그 데이터를 저장하고 location 을 외래키로 사용하여 User 테이블과 1:N 관계로 만들고 싶었습니다. 그러기 위해선 Yahoo 의 날씨 API 를 사용해서 location 을 woeid 로 바꿔야했는데, 몇달 전부터 Yahoo 가 이 기능을 더이상 지원하지 않는다는 겁니다...! 그래서 다른 방법을 찾아봤지만 없었고, 울며 겨자먹기로 10여개의 중요 나라들의 woeid 들을 수동으로 입력해 놨습니다. 그렇기 때문에 User 테이블과 Trend 테이블의 1:N 관계는 적절히 설정하지 못했습니다. 그래도, 트랜딩 토픽을 보여주고 저장하는 기능엔 문제가 없습니다 (다만 야후가 야속할뿐...). 트위터 API 는 트랜딩 토픽을 출력하기 위해서 woeid 를 요구하기때문에 어쩔 수 없이 수동으로 넣어줘야 했습니다! 
