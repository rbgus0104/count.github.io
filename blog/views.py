from django.shortcuts import render,redirect
from .models import Post


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    text=request.GET['fulltext']
    K = text.split()
    dic = {}
    for word in K:
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1
    return render(request, 'result.html',{'full':text, 'num':len(K), 'dict': dic.items()})



