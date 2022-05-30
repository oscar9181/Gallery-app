from django.shortcuts import render,redirect

# Create your views here.


# def base(request):
#     return render(request,'gallery/base.html')


def home(request):
    return render(request, 'pictures/home.html')

def viewPicture(request,pk):
    return render(request,'pictures/display.html')

def addPicture(request):
    return render(request,'pictures/add.html')