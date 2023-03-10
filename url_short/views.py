from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Url
from .forms import UrlForm

import random
import string

# Create your views here.

def urlShort(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
            url = form.cleaned_data["url"]
            new_url = Url(url=url, slug=slug)
            new_url.save()
            
            return redirect('home')
    else:
        form = UrlForm()

    data = Url.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'url_short/index.html', context)


def urlRedirect(request, slugs):
    data = Url.objects.get(slug=slugs)
    return redirect(data.url)