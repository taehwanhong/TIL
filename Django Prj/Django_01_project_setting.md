## 환경 설정


### Project init

### pyenv 생성

** {{ }} 안의 이름은 원하는대로 정하시면 됩니다. 다만 {{ }} 안에 같은 이름이 있는 경우 같은 이름으로 넣어주세요. **

### 독립환경 설정하기 (Virtual Environment)

1. pyenv-virtualenv 라이브러리 설치: brew install pyenv-virtualenv

2. 터미널 시작 시 자동 반영: echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

3. 즉각 반영: source ~/.bash_profile

4. 폴더 생성: mkdir {{ python_project }}

5. 폴더 들어가기: cd {{ python_project }}

6. 파이썬 3.5.2버전 독립환경 설정: pyenv virtualenv {{ my_python }}

7. 독립환경 실행: pyenv activate {{ my_python }}

### 장고 설치

1. 장고 설치하기: pip install django

2. 새로운 프로젝트 만들기: django-admin startproject {{firstsite}}

3. 기본 데이터베이스 설정하기: python manage.py migrate

4. 로컬 서버 시작하기: python manage.py runserver

5. 로컬 서버 종료: CONTROL + C


## Default Setting for each project

1.  새로운 폴더 생성 후 독립 환경 설정

- pip install --upgrade pip
- pip install django
- django-admin startproject baemin
- 가장 상단의 baemin 폴더 src 로 이름 변경
- python manage.py migrate
- python manage.py startapp client
- python manage.py startapp partner

- 기존 프로젝트에서 templates 폴더 만들고, base.html 복사하기

- 기존 프로젝트에서 static 폴더 통째로 복사하기
- baemin/settings.py 파일 안 세팅 수정하기 (기존 프로젝트 참고)
- INSTALLED_APPS 리스트 안에 'client', 'partner' 넣기
- TEMPLATES 안 'DIRS' 리스트 안에 os.path.join(BASE_DIR, "templates")
- 가장 하단에 STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static") ] 추가
- 깃허브에 프로젝트 올리기
- README.md 파일 만들고, git init 이후, git add . 로 전체 파일 추가하기
- .gitignore 파일 만들고, 아래 목록 각각 추가
- db.sqlite3
- baemin_sample/ (독립 환경 생성 시 만들어지는 폴더 이름)
- git commit -m "first commit" 부터 남은 설정 진행 
