from Shop.models import Product,Contact
from django.shortcuts import render
from django.http import HttpResponse
from math import ceil

# Create your views here.
def index(request):
    # products=Product.objects.all()
    # print(products)
    # n=len(products)
    # nslides=n//4+ceil((n/4)-(n//4))
    # params={'no_of_slides':nslides,'range':range(1,nslides),'products':products}
    
    # allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]

    allprods=[]
    catprods=Product.objects.values("category","id")
    cats={item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nslides),nslides])

    params={"allprods":allprods}
    return render(request,"Shop/index.html",params)

def about(request):
    return render(request,"Shop/about.html")

def contact(request): 
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

    return render(request,"Shop/contact.html")


def tracker(request):
    return render(request,"Shop/tracker.html")


def search(request):
    return render(request,"Shop/search.html")


def productview(request,myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request,"Shop/prodView.html",{"product":product[0]})

def checkout(request):
    return render(request,"Shop/checkout.html")


def scrap(request):
    return render(request,"Shop/scrap.html")

def eservice(request):
    return render(request,"Shop/eservice.html")

def pservice(request):
    return render(request,"Shop/pservice.html")