from django.shortcuts import render

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
    
    context={
        "status_home":"",
        "status_screams":" class="+active,#highlights screams in navbar
        }
    
    return render(request,'home/screams.html',context)


