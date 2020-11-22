from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Home

def home(request):
    form=Home()
    return render(request, 'home.html',{'form': form})

