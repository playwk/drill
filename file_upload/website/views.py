from django.shortcuts import render, HttpResponse, render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from  django import forms
from website.forms import MomentForm
import os
# Create your views here.



def index(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        f = open(os.path.join('data', file.name), 'wb')
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('OK!')
    return render(request, 'index.html')


def disk(request):
    if request.method == "POST":
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            return HttpResponse('Upload OK!')
    else:
        uf = UserForm()
    return render_to_response('disk.html', {'uf': uf})

def welcome(request):
    return HttpResponse('<h1>欢迎你！</h1>')

def moment_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse('welcome'))
    else:
        form = MomentForm()
    PROJECT_ROOT =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(PROJECT_ROOT)
    print(form)
    return render(request, os.path.join(PROJECT_ROOT, 'templates', 'moment_input.html'),
                  {'form': form})
