from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import Screams
# Create your views here.


def home(request):
    active="active"
    
    context={
        'message1':"Welcome to Screambox",
        'message2':"scream here",
        "status_home":" class="+active, #highlights home in top navbar
        "status_screams":"",
        }
    
    return render(request,'home/index.html',context)


def screams(request):

    active="active"
    screams=Screams.objects.all()
    
    context={
        "screams":screams,
        "status_home":"",
        "status_screams":" class="+active,#highlights screams in navbar
        }
    
    return render(request,'home/screams.html',context)



def screaming(request):
    a=Screams()
    a.scream=request.POST.get('inputtext', '')
    a.screamer="anonymous"
    
        
    
    
    active="active"
    screams=Screams.objects.all()
    if a.scream =='':
        context={
        'message1':"Welcome to Screambox",
        'message2':"sorry! we didnt hear you",
        "status_home":" class="+active, #highlights home in top navbar
        "status_screams":"",
        
            }
        return render(request,'home/index.html',context)
    else:
        a.save()
        context={
            "screams":screams,
            "status_home":"",
            "status_screams":" class="+active,#highlights screams in navbar
            }
        
        
        return render(request,'home/screams.html',context)


class ScreamsCreate(CreateView):
    model = Screams
    
    fields=["scream"]









