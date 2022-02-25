from django.shortcuts import render, redirect, get_object_or_404
from .forms import UrlForm
from .models import UrlLink


def home(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            new_link = form.save(commit=False)
            new_link.original_url = form.cleaned_data['url']
            new_link.short_url = form.generate_short_url(new_link.original_url)
            new_link.save()

            return redirect('home')
            
    else:
        form = UrlForm()
    return render(request, 'home.html', {'form':form})


def redirect_to_link(request, shrt_url):
    relation = get_object_or_404(UrlLink, short_url = shrt_url)
    website = relation.original_url
    redirect_url = "http://" + website + "/"
    return redirect(redirect_url)
