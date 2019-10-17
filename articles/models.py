from django.db import models
from django.core.validators import EmailValidator, MinValueValidator

# Create your models here.

class Article(models.Model):  # model명은 단수로! app 이름은 보통 복수로!
    title = models.CharField(max_length=20)  # max_length: 필수적으로 들어가야함!
    content = models.TextField()  # TextField로 하는 이유: 내용이 길 수 있어서
    created_at = models.DateTimeField(auto_now_add=True)  # 날짜와 시간 동시저장
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  # 데이터를 위한 데이터
        ordering = ('-pk', )  # tuple로 인식하도록 ,를 붙인다
        # 새로 만든 애들이 위쪽으로 쌓일 수 있도록

# 모델링 했다고 장고에게 알려주러 간다.
# $ python manage.py makemigrations -> 알려줌(실제 db에 반영시키지 않음)
        # 이때, content내용이 없어도 에러나지 않음
# $ python manage.py migrate -> 실제 db에 넣음

# 이미 만들어져있는 db에 항목 추가하려면 class에 나중에 content 추가해서 넣으려면 
# $ python manage.py makemigrations
# 1
# ''  #실제 db에 반영된 것은 아님
# $ python manage.py migrate  -> 반영


class Person(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(
        max_length=100,
        validators=[EmailValidator(message='이메일 형식에 맞지 않습니다.')]
    )
    age = models.IntegerField(
        validators=[MinValueValidator(19, message='미성년자는 노노')]
    )


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
            # on_delete 설정 : 참조한 키가 삭제되면 그 키와 관련된 데이터를 같이 삭제해주세요
    class Meta:  # 데이터를 위한 데이터
        ordering = ('-pk', )  # 1. tuple로 인식하도록 ,를 붙인다
                              # 2. 새로 만든 애들이 위쪽으로 쌓일 수 있도록
