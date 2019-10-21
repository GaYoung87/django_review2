from django.urls import path
from . import views
app_name = 'accounts'

# urlpatterns가 있어야 error가 안남 -> list 우선적으로 만들자!
urlpatterns = [
    # 회원가입 url
    path('signup/', views.signup, name='signup'),
    # 로그인 url
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
