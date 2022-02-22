from django.shortcuts import render, redirect
from .forms import UrlForm

def home(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            new_link = form.save(commit=False)
            new_link.short_url = 5
            new_link.original_url = form.cleaned_data['url']
            new_link.save()

            return redirect('home')
            
    else:
        form = UrlForm()
    return render(request, 'home.html', {'form':form})


def create(request, id):
    print("helllllloooooooo")
    return redirect('home')