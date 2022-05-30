from django.shortcuts import render,redirect
from.models import Category,Pictures

# Create your views here.


# def base(request):
#     return render(request,'gallery/base.html')


def home(request):
    categories = Category.objects.all()
    picture = Pictures .objects.all()
    
    context = {'categories': categories,'pictures':picture}
    return render(request, 'pictures/home.html',context)
     
def viewPicture(request,pk):
    return render(request,'pictures/display.html')

def addPicture(request):
    return render(request,'picture/add.html')