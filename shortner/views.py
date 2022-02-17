from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def create(request, id):
    print("helllllloooooooo")
    return redirect('home')