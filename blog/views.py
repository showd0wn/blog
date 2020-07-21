from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html', context={
        'title': '卿志宇的网络日志',
        'welcome': 'Welcome~'
    })
