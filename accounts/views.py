from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect, render
from .models import Profile

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        #요청한 유저가 실제로 있는지 확인하는 과정- 두개가 일치하면 객체를 가져오고 아니면 반환

        if user is not None:
            auth.login(request, user)#로그인 처리
            return redirect('main:postpage')#이 postpage로 이동
        else:
            return render(request, 'accounts/login.html')#none이면 login.html을 보여준다
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')#login.html을 보여준다

def logout(request):
    auth.logout(request)#현재 로그인되어 있는 유저 로그아웃처리
    return redirect('main:postpage')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/signup.html')#중복아이디 처리 과제
    
        if request.POST['password'] == request.POST['confirm']:
            newuser = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )

            nickname = request.POST['nickname']
            major = request.POST['major']
            recommender_code = request.POST['recommender_code']#추가한 과제
            profile_image = request.FILES.get('profile_image')

            profile = Profile(
                user=newuser,
                nickname=nickname,
                major=major,
                profile_image=profile_image,
                recommender_code= recommender_code,#추가한과제
            )
            profile.save()

            auth.login(request, newuser)
            return redirect('main:postpage')
        
    return render(request, 'accounts/signup.html')


# Create your views here.
