from django.shortcuts import render,redirect
from.models import Category,Pictures

# Create your views here.


# def base(request):
#     return render(request,'gallery/base.html')


def home(request):
    categories = Category.objects.all()
    pictures = Pictures .objects.all()
    
    context = {'categories': categories,'pictures':pictures}
    return render(request, 'pictures/home.html',context)
     
def viewPicture(request,pk):
    album = Pictures .objects.get(id=pk)
    return render(request,'pictures/display.html',{'album' : album})

def addPicture(request):
    return render(request,'pictures/add.html')