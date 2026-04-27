from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def mainpage(request):
    context = {
        'generation': 14,                   
        'info': {                           
            'who': '차은호님',
            'mentor': '수현님, 유미님',
            'note': '피드백 대환영입니당'
        },
        'shortcuts': [
            '2주차는 html을 작성하기 위해 tamplates폴더를 먼저 생성',
            'mainpage를 tamplates 폴더 안에 만들고 view.py를 작성해서 페이지에 보여지게 만든다',
            'url을 작성해서 mainpage 매서드와 연결하고 이를 테스트 해보면 홈페이지가 보임',
            'secondpage도 이와 동일하게 진행',
            '변수사용을 통해 템플릿의 언어를 변경',     
            'main과 second의 중복되는 내용들을 base.html로 묶어 이 두개에 상속시킨다',          
            '정적파일 폴더를 생성해서 base에 css를 연결, main에 image를 넣는다'
            '이를 setting.py에 경로를 설정하면 이번주차 세션 요약 끝!!'
        ]
    }
    return render(request, 'main/mainpage.html', context)

def new_post(request):
    return render(request, 'main/new_post.html')

def postpage(request):
    posts = Post.objects.all()
    return render(request, 'main/postpage.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.view_count += 1
    post.save()
    return render(request, 'main/detail.html', {'post': post})

def edit(request, post_id):
    edit_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'main/edit.html',{"post":edit_post})

def create(request):
    new_post = Post()

    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = request.POST['pub_date']
    new_post.content =request.POST['content']

    new_post.save()

    return redirect('main:detail', new_post.id)

def update(request, post_id):
    update_post = get_object_or_404(Post, pk=post_id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.pub_date = request.POST['pub_date']
    update_post.content = request.POST['content']
    update_post.save()

    return redirect('main:detail', update_post.id)

def delete(request, post_id):
    delete_blog = get_object_or_404(Post, pk=post_id)
    delete_blog.delete()

    return redirect('main:postpage')
    


def secondpage(request):
    second_context = {
        'generation': 14,                   
        'info': {                           
            'name': '이승우',
            'mentor': '수현님, 유미님',
            'note_2': '아래에서 소개할께요'
        },
        'shortcuts_2': [
            '일단 나이 26살 만으로는 24살',
            '좋아하는 것은 운동,게임,음악 듣는거, 음식 맛있는거 좋아하구요 (음식이랑 운동은 거의 안가립니다) ',
            '보드게임은 카탄?이랑 뱅, 할리갈리 같은거 해봤습니다',
            '개발은 거의 처음 해봐요',
            '2주차까지 세션을 진행했는데 동아리에 들어오길 잘했다는 생각이 들어요',     
            '앞으로도 열심히 할테니까 많이 알려주시면 감사하겠습니다',          
            '좋은 하루 되세요!!'
            '--자기소개 끝--'
        ]
    }
    return render(request, 'main/secondpage.html',second_context)