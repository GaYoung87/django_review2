from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# UserCreationForm을 통해 user에 대한 정보 가지고옴
from django.contrib.auth import login as auth_login, logout as auth_logout
# Authentication에 대한 행위를 할 수 있음 import login으로 로그인할 수 있음.
from django.views.decorators.http import require_POST

# 회원가입 form이 제공되어야함
# get: 처음에 signup 눌렀을 때 
# post: form 작성하고나서 가입하기 누르면 post로 이동

def signup(request):
    if request.user.is_authenticated:  # 인증상태라면
        return redirect('articles:index')
    # request.user.username == base.html에서 user.username
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # 사용자가 form안에서 id랑 비밀번호 입력한 것
        if form.is_valid():  # 입력값 확인
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:  # == 'GET'
        form = UserCreationForm
    context = {'form': form}
    # 회원가입 페이지 주세요
    return render(request, 'accounts/signup.html', context)


def login(request):  # from django.contrib.auth import login과 이름이 같다.
    # POST: 로그인 시켜줌
    if request.method == 'POST':
        # 로그인 로직
        form = AuthenticationForm(request, request.POST)  # AuthenticationForm에만 첫번째 인자로 request가 들어간다.
        if form.is_valid():
            auth_login(request, form.get_user())  # 사용자의 정보를 주는 함수: form.get_user()
            next_page = request.POST.get('next')
            return redirect(next_page or 'articles:index')

    else:  # GET: 로그인 페이지 보여줌
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


# 로그아웃: sessionid 지우기
# 세션에 대한 데이터 저장공간: 쿠키
# session: user라는 데이터 하나 만들기
def logout(request):  # logout에는 login_required가 필요 없다!
    auth_logout(request)
    return redirect('articles:index')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')
