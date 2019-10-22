from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model  # 현재 활성화(adcive)된 user model을 return 한다.


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        # 원래 default user model이 있는데, 나중에 우리가 customize한 usermodel이 생길 수 있음 
        # -> default user model 안쓰면 그때부터 get_user_model()이 default값이 아니게 됨
        # models.py에서는 get_user_model()사용하지 않음
        fields = ['email', 'first_name', 'last_name', ]
