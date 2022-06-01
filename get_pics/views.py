from django.shortcuts import render
from.models import Category,Pictures


def home(request):
    
    category = request.GET.get('category')
    if category == None:
        pictures = Pictures.objects.all()
    else:
        pictures = Pictures.objects.filter(category__name=category)
        
        
    categories = Category.objects.all()
    
    
    context = {'categories': categories,'pictures':pictures}
    return render(request, 'pictures/home.html',context)
     
def viewPicture(request,pk):
    picture = Pictures .objects.get(id=pk)
    return render(request,'pictures/display.html',{'picture' : picture})


def searchPicture(request):
    query = request.GET.get('query')
    if query != None:
        pictures = Pictures.objects.filter(category__name=query)
    context = {
        'pictures': pictures,
        'title':'search pictures'
    }
    return render(request, 'pictures/search.html', context)