from django.shortcuts import render

from .forms import SmForm
from .models import SmModel




def home(request):
    return render(request,'index.html',{"text":SmForm})