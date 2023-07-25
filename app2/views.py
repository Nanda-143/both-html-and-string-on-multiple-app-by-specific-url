from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def third(request):
    return render(request,'third.html')
def four(request):
    return render(request,'four.html')
def run(request):
    return HttpResponse('this is done from app2')
