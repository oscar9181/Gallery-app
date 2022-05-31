from django.shortcuts import render,redirect
from.models import Category,Pictures


def home(request):
    categories = Category.objects.all()
    pictures = Pictures .objects.all()
    img_url = []
    for p in pictures:
        img_url.append(p.image)
    print(img_url)
    
    context = {'categories': categories,'pictures':pictures}
    return render(request, 'pictures/home.html',context)
     
def viewPicture(request,pk):
    picture = Pictures .objects.get(id=pk)
    return render(request,'pictures/display.html',{'picture' : picture})


def searchPicture(request):
    query = request.GET.get('query')
    if query != None:
        picture = Pictures.objects.filter(category__name=query)
    context = {
        'image': picture,
        'title':'search photos'
    }
    return render(request, 'pictures/search.html',context)