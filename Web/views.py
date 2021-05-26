from django.shortcuts import render
from .models import video
from .models import video2
from .forms import videoForm
from .forms import videoForm2
from subprocess import run, PIPE
import sys

# Create your views here.
def index(request):
    if request.method == "POST":
        form = videoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            vid1 = video.objects.last()
            p = vid1.video1
            q = vid1.video2
            #print(p,q)
            out = run([sys.executable, 'media/python/frames.py',str(p)], shell=True, stdout=PIPE)
            out1 = run([sys.executable, 'media/python/deepfake.py',str(q)], shell=True, stdout=PIPE) 
            return render(request, "index.html",{"form":form,"video":vid1,"p":p,"q":q})
    else:
        form = videoForm()
    return render(request, 'index.html',{"form":form})

def index2(request):
    if request.method == "POST":
        form1 = videoForm2(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            vid2 = video2.objects.last()
            r = vid2.image
            s = vid2.video3
            #print(p,q)
            out1 = run([sys.executable, 'media/python/deepfake2.py',str(r),str(s)], shell=True, stdout=PIPE) 
            return render(request, "display.html",{"form":form1,"video":vid2,"r":r,"s":s})
    else:
        form1 = videoForm2()
    return render(request, 'display.html',{"form":form1})