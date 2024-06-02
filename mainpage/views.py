
from django.views import generic
from django.shortcuts import render
from django.utils import timezone
# Create your views here.
def Index(request):
    return render(request, 'mainpage/index.html')