from django.shortcuts import render, redirect
from .forms import UrlForm
import uuid
from .models import Url
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'form': UrlForm()})

def create(request):
    if request.method == 'POST':
        link = request.POST['link_url']
        uid = str(uuid.uuid4())[:10]
        new_url = Url(link_url=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def find_url(request, pk):
    try:
        url_detail = Url.objects.get(uuid=pk)
    except:
        url_detail = None
    
    if url_detail is not None:
        return redirect(url_detail.link_url)
    else:
        return redirect('index')
