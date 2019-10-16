from django.shortcuts import render, redirect, get_object_or_404
    # get_object_or_404: 꺼내는데, 거기에 해당하는데이터 없으면 404status코드 제공까지 알아서해줌
from .forms import ArticleForm
from .models import Article
# from IPython import embed  # 너무 개발용..
from django.views.decorators.http import require_POST, require_GET


@require_GET
def index(request):
   articles = Article.objects.all()
   context = {'articles':articles}
   return render(request, 'articles/index.html', context)


@require_GET
def detail(request, article_pk):
    # 사용자가 url에 적어보낸 article_pk를 통해 디테일 페이지를 보여준다.
    # 특정 한개의 article을 꺼내는 방법
    # 방법1.
        # model이용: Article.objects.get(pk=article_pk)  
    # 방법2.
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)
        # return render(request, 'articles/detail.html', {'article': article})해도 위와 동일
        # 시험에 나올 수 있음!



# get: 사용자는 우리에게 작성할 수 있는 html페이지를 받아감
# post: 우리에게 받은 form(작성하는 페이지)에서 실제로 db에 작성하겠다는 것
def create(request):
    if request.method == 'POST':
        # Article을 생성해달라고 하는 요청
        # 데이터 거내서 Article 생성
        # 실제적으로 데이터를 생성.
        form = ArticleForm(request.POST)  # 사용자의 데이터를 가지고오겠다.
        # embed()  # 잠시 코드멈춰서 shell에 들어갔다가 나오면 다시 코드 진행
                 # 데이터까지 적혀있는 것을 보여줌 
        if form.is_valid():  # 유효하지 않으면 else문가서 context에 가서 다시 rendering
            form.save()
            return redirect('articles:index')
        
    else: 
        # GET 요청
        # Article을 생성하기 위한 페이지를 달라고 하는 요청
        # 브라우저에서 생성하고 엔터치면 나오는 페이지 보여줌
        form = ArticleForm()  # 비어있는 form
    context = {'form': form}
    return render(request, 'articles/create.html', context)  
            # templates 안에 있는 articles 폴더에 있는 create로 보내라
                # -> templates/articles/create.html에서 templates가 빠져있다고 생각!

# form: 우리가 정의한대로
# model form: form.save()하면 데이터 따로 뽑아낼 필요없이 form으로 한번에 저장

# create함수와 동일. 그러나 중복되는 부분 줄일 수 있으므로 위와같이 작성
# def create(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('articles:index')
#         else:
#             context = {'form': form}
#             return render(request, 'articles/create.html', context)
        
#     else: 
#         form = ArticleForm()
#         context = {'form': form}
#         return render(request, 'articles/create.html', context) 


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)  # 기존에 존재하는 data에 추가
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk)
    else:  # GET method
        form = ArticleForm(instance=article)  # 특정 데이터를 넣은 채로 form을 보이겠다.
    context = {'form': form}
    return render(request, 'articles/update.html', context)
    # get : update를 이제 할 것이다 -> update페이지 여기있어
    # post: 수정하려고 데이터 들고왔구나, 원하는데로 수정해줄께. detail page로 보냄


@require_POST  # post요청 들어왔을 때만 가능!
               # get요청으로 들어오면 사용자가 이상한 방법으로 삭제하려고 한 것이다.
# articles/3/delete 를 직접 입력하면 삭제됨. -> 이를 방지해야함!!!
def delete(request, article_pk):
    # article_pk에 맞는 article을 꺼낸다.
    # 삭제한다. (POST, form 사용이유: 우리가 제공하는 방법으로만 삭제하게 만들기 위해!)
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
