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
    categories = Category.objects.all()
    
    if request.method == 'POST':
       data = request.POST
       image = request.FILES.get('image')
       
    if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
    elif data['category_new'] !='':
            category,created =  Category.objects.get_or_create(name=data['category_new'])  
            
    else: 
            category = None   
            
    image = Pictures.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )     
    

    
    
    context = {'categories': categories}
    return render(request,'pictures/add.html',context)