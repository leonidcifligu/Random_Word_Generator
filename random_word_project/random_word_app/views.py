from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] +=1
        request.session['random'] = get_random_string(length=14)
        return render(request,"index.html")

def generate(request):
    if request.method == 'POST':
        return redirect("/")

def reset(request):
    if request.method == "POST":
        request.session['counter'] = 0
    return redirect("/")
