from django.shortcuts import render, redirect
import requests
from django.contrib import messages

def index(request):
    return render(request, 'index.html')