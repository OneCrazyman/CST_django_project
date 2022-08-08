from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>정재훈 이새1키 왜 견적 맞추러 신창까지옴?</h1>")