from django.shortcuts import render
from django.http import HttpResponse
from .models import WeChatUser, Status
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


# Create your views here.
def home(request):
    return render(request, 'homepage.html')


@login_required
def show_user(request):
    return render(request, 'user.html', {
        'user': {
            'name': 'ctct',
            'motto': '123456',
            'email': 'ct@qq.com',
            'pic': 'Po2.jpg'
        }
    })


@login_required
def show_status(request):
    statuses = Status.objects.all()
    # import pdb
    # pdb.set_trace()
    return render(request, 'status.html', {'statuses': statuses})


@login_required
def submit_post(request):
    user = WeChatUser.objects.get(user=request.user)
    text = request.POST.get('text')
    uploaded_file = request.FILES.get("pics")
    if uploaded_file:
        name = uploaded_file.name
        with open("./moments/static/image/{}".format(name), 'wb') as handle:
            for block in uploaded_file.chunks():
                handle.write(block)
    else:
        name = ''
    if text:
        status = Status(user=user, text=text, pics=name)  # 注意此处有改动
        status.save()
        return redirect('/status')
    return render(request, 'my_post.html')
