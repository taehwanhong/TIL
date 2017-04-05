# Django 를 이용한 REST Framework 생성하기.

1. 장고 등 관련 패키지를 설치한다.
    - pyenv로 진입
    - restframework 관련 package설치
    > pip install django
    > pip install djangorestframework
    - 프로젝트 시작
    > django-admin startproject rest
    - APP시작
    > django-amdin startapp jinnycast
요까지 하면 아래와 같은 디렉토리를 만든다.

```
db.sqlite3 manage.py  rest
(tutorial) ➜  rest git:(betaDjango) ✗ tree
.
├── db.sqlite3
├── manage.py
└── rest
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-35.pyc
    │   ├── settings.cpython-35.pyc
    │   ├── urls.cpython-35.pyc
    │   └── wsgi.cpython-35.pyc
    ├── jinnycast
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── quickstart(여기는 연습용이니 무시하셈)
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-35.pyc
    │   │   ├── serializers.cpython-35.pyc
    │   │   └── views.cpython-35.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   └── views.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

7 directories, 28 files
```

3. 각종 셋팅을 한다.
 1. 각종 셋팅 1번
  - installed app에 rest framework등록하고, rest framework 작동하도록 셋팅하기.
  - settings.py 
```
 INSTALLED_APPS = [
    'rest_framework',
    'jinnycast',
]
```

 - 아래 코드의 역할은 뭔지 공부해야함.
```
  REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10,
}
```

 2. 각종 셋팅 2번
  - 모델을 생성해줘야함.
  - jinnycasy/models.py
  - 아직 아래 코드가 뭔지 모르겠다. 아마도 DB셋팅하는거같아보임
```
# Create your models here.

from django.db import models


class Jinnycast(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=20, blank=True, default='')
    pw = models.CharField(max_length=12, blank=True, default='')
    content = models.TextField()

    class Meta:
        ordering = ('created',)

```

  - jinnycast/admin.py
  # Register your models here.

from django.contrib import admin
from bbs.model import Bbs

class BbsAdmin(admin.ModelAdmin):
    list_display=('title','author','created',)

admin.site.register(Bbs, BbsAdmin)



4. 서버를 띄운다.
5. 완성
