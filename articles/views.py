from django.shortcuts import render

# get: 사용자는 우리에게 작성할 수 있는 html페이지를 받아감
# post: 우리에게 받은 form(작성하는 페이지)에서 실제로 db에 작성하겠다는 것
def create(request):
    if request.method == 'POST':
        # Article을 생성해달라고 하는 요청
        pass
    else:  # GET 요청
        # Article을 생성하기 위한 페이지를 달라고 하는 요청
        return render(request, 'articles/create.html')  
            # templates 안에 있는 articles 폴더에 있는 create로 보내라
                # -> templates/articles/create.html에서 templates가 빠져있다고 생각!