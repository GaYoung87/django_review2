# review에서 articles로 보내라했기 때문에 articles에서도 urls.py가 있어야 에러가 안남. 
from django.urls import path
from . import views  # 현재 app에서 view를 가지고오겠다 -> .=현재 앱
urlpatterns = [
    path('create/', views.create, name='create'),
        # 여러 앱에서 create라는 함수가 있을 수 있는데, 이름을 지정하면 이름이 나올 때 가라!
]
