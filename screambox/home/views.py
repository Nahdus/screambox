from django.shortcuts import render

# Create your views here.


def home(request):
    
    context={
        'message1':"Welcome to Screambox",
        'message2':"scream here",
        }

    return render(request,'home/index.html',context)
'''

def screams(request):
    
    return render(request,'home/screams.html')

'''
