# Django crud 구축하기

<hr/>

##  1. 가상 환경 생성 및 적용

```bash
# 1) 파이썬 버전 확인
# 반드시 3.7.x 버전이 맞는지 확인 후 진행
$ python -V
Python 3.7.4
# 2) 가상환경 생성
# python -m venv <가상환경 설치 경로>
$ python -m venv venv
# 3) 가상환경 적용
$ source venv/Scripts/activate
# 4) 버전 확인
(venv) # <- 가상환경 적용 시 git bash에서 해당 환경 이름이 표시된다.
$ python -V
Python 3.7.4
# 5) 설치된 모듈 확인
(venv)
$ pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
# 6) pip upgrade
(venv)
$ python -m pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/8d/07/f7d7ced2f97ca3098c16565efbe6b15fafcba53e8d9bdb431e09140514b0/pip-19.2.2-py2.py3-none-any.whl (1.4MB)
    100% |████████████████████████████████| 1.4MB 7.3MB/s
Installing collected packages: pip
  Found existing installation: pip 19.0.3
    Uninstalling pip-19.0.3:
      Successfully uninstalled pip-19.0.3
Successfully installed pip-19.2.2
# 7) pip upgrade 확인
(venv)
$ pip list
Package    Version
---------- -------
pip        19.2.2
setuptools 40.8.0
```

<br/>

```bash
# requirments.txt에 있는 것만 설치
# 1) pip list 확인
$ pip list
Package    Version
---------- -------
Django     2.2.6
pip        19.3
pytz       2019.3
setuptools 40.8.0
sqlparse   0.3.0

# 2) pip freeze > requirements.txt 보이기
$ pip freeze > requirements.txt
(venv)

# 3) 이미 설치되어있는 것 삭제!
$ pip freeze | xargs pip uninstall -y
Uninstalling Django-2.2.6:
  Successfully uninstalled Django-2.2.6
Uninstalling pytz-2019.3:
  Successfully uninstalled pytz-2019.3
Uninstalling sqlparse-0.3.0:
  Successfully uninstalled sqlparse-0.3.0
(venv)

# 4) 삭제한 것 확인
$ pip list
Package    Version
---------- -------
pip        19.3
setuptools 40.8.0
(venv)

# 5) pip install -r requirements.txt에 있는 것만 설치
$ pip install -r requirements.txt
```

<br/>

## 2. 환경 세팅

```python
# 1) 인터프리터 설정
Ctrl + Shift + P -> Python: Select Interpreter 선택

    
# 2) 환경 변수 세팅
{
    "python.pythonPath": "venv\\Scripts\\python.exe",
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    "emmet.includeLanguages": {"django-html": "html"},
    "[django-html]": {
        "editor.tabSize": 2
    }
}
```

<br/>
<br/>

## 3. django project 시작

```bash
# 1) django 모듈 설치
(venv)
$ pip install django
```

- Django를 설치한 순간부터 `django-admin`이라는 command를 사용할 수 있게 된다.
- 이 command를 통해 django project에 여러가지 명령을 할 수 있다.

```bash
# 2) start project
(venv)
$ django-admin startproject myproject .
```

- 현재 디렉토리에서 myproject라는 이름으로 프로젝트를 시작하겠다는 뜻.

- python과 django에서 이미 사용되는 이름은 사용하지 않는다.
  (django라는 이름은 django 그 자체와 충돌이 발생하며, test라는 이름도 django 내부적으로 사용하는 모듈 이름)
- 프로젝트명 뒤에 .을 반드시 적어야 한다.

```bash
# 3) make app
(venv)
$ python manage.py startapp articles
```

- manage.py를 통해 앱을 생성한다.

## 4. settings.py 설정

```python
# 1) app 등록
INSTALLED_APPS = [
    # Local apps
    'articles',
    
    # Third party apps
    'django_extensions',
    
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- app을 만든 후 INSTALLED_APPS에 등록해 준다.
  <br/>:star:

```python
# 2) 언어 및 시간대 설정
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True  # False라고 적었으면, 아무리 ko-kr해도 영어로 나옴!(번역하지 않겠다.)
                 # True라고 해야 원하는 언어로 볼 수 있음!
```

<br/>

## 5. app의 models.py 설정 :star:

````python
from django.db import models

# Create your models here.

class Article(models.Model):  # model명은 단수로! app 이름은 보통 복수로!
    title = models.CharField(max_length=20)  # max_length: 필수적으로 들어가야함!
    created_at = models.DateTimeField(auto_now_add=True)  # 날짜와 시간 동시저장
    updated_at = models.DateTimeField(auto_now=True)

# 모델링 했다고 장고에게 알려주러 간다.
# $ python manage.py makemigrations -> 알려줌(실제 db에 반영시키지 않음)
        # 이때, content내용이 없어도 에러나지 않음
# $ python manage.py migrate -> 실제 db에 넣음

# 이미 만들어져있는 db에 항목 추가하려면 class에 나중에 content 추가해서 넣으려면
	# 1. content항목 넣기
    # 2. 다시 python manage.py makemigrations -> 1 -> ''(default값으로 ''을 지정)
    # 3. python manage.py migrate -> 실제 db에 넣음 
content = models.TextField  # TextField로 하는 이유: 내용이 길 수 있어서
````

- 값을 넣는 방법 : shell_plus해서 값 추가(우리가 선택한 것):star:

```bash
# 이미 있는 model에 내용 추가
python manage.py shell_plus
# Shell Plus Model Imports
from articles.models import Article
In [1]: Article
Out[1]: articles.models.Article

In [2]: article = Article()

In [3]: article.title = '첫번쩨 타이틀'

In [4]: article.save()

In [5]: article
Out[5]: <Article: Article object (1)>

In [6]: article.pk
Out[6]: 1

In [7]: article2 = Article()

In [8]: article.title = '두번째 아티클'

In [9]: article.save()

In [10]: exit()
```

