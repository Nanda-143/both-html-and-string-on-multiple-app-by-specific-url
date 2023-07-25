from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def five(request):
    return render(request,'five.html')
def six(request):
    return render(request,'six.html')
def nothing(request):
    return HttpResponse('this is done from app3')
