from django.shortcuts import render, redirect
from ipware import get_client_ip
from .models import user, Items, shipping_info
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    #find or create object according user Ip address
    currentip=get_client_ip(request)[0]
    userperson=user.objects.get_or_create(ipaddress=currentip)
    userperson=userperson[0]

    if request.method=='POST':
        resultlist=list(request.POST)
        if "Jordan1" in resultlist:
           productobj=Items.objects.get(id=2)
           userperson.item.add(productobj)
           number=int(request.POST["Jordan1"])
           userperson.quanity2=number
           userperson.save()


        if "retro" in resultlist:
           productobj=Items.objects.get(id=1)
           userperson.item.add(productobj)
           number = int(request.POST["retro"])
           userperson.quanity1 = number
           userperson.save()

        if "jordan3" in resultlist:
            productobj = Items.objects.get(id=4)
            userperson.item.add(productobj)
            number = int(request.POST["jordan3"])
            userperson.quanity4 = number
            userperson.save()

        if "jordan4" in resultlist:
            productobj = Items.objects.get(id=3)
            userperson.item.add(productobj)
            number = int(request.POST["jordan4"])
            userperson.quanity3 = number
            userperson.save()
    allitems=userperson.item.all()
    context={"allitems": allitems,
             "one": userperson.quanity1,
             "two": userperson.quanity2,
             "three": userperson.quanity3,
             "four": userperson.quanity4}

    return render(request, 'index.html', context)

def cart(request):
    currentip = get_client_ip(request)[0]
    userperson = user.objects.get_or_create(ipaddress=currentip)
    userperson = userperson[0]

    if request.method == 'POST':
        resultlist = list(request.POST)
        if "Jordan1" in resultlist:
            productobj = Items.objects.get(id=2)
            userperson.item.add(productobj)
            number = int(request.POST["Jordan1"])
            userperson.quanity2 = number
            userperson.save()

        if "retro" in resultlist:
            productobj = Items.objects.get(id=1)
            userperson.item.add(productobj)
            number = int(request.POST["retro"])
            userperson.quanity1 = number
            userperson.save()

        if "jordan3" in resultlist:
            productobj = Items.objects.get(id=4)
            userperson.item.add(productobj)
            number = int(request.POST["jordan3"])
            userperson.quanity4 = number
            userperson.save()

        if "jordan4" in resultlist:
            productobj = Items.objects.get(id=3)
            userperson.item.add(productobj)
            number = int(request.POST["jordan4"])
            userperson.quanity3 = number
            userperson.save()
    allitems = userperson.item.all()
    context = {"allitems": allitems,
               "one": userperson.quanity1,
               "two": userperson.quanity2,
               "three": userperson.quanity3,
               "four": userperson.quanity4}
    return render(request, 'cart.html', context)

def shippinginfo(request):
    currentip = get_client_ip(request)[0]
    userperson = user.objects.get_or_create(ipaddress=currentip)
    userperson = userperson[0]

    if request.method == 'POST':
        resultlist = list(request.POST)
        if "Jordan1" in resultlist:
            productobj = Items.objects.get(id=2)
            userperson.item.add(productobj)
            number = int(request.POST["Jordan1"])
            userperson.quanity2 = number
            userperson.save()

        if "retro" in resultlist:
            productobj = Items.objects.get(id=1)
            userperson.item.add(productobj)
            number = int(request.POST["retro"])
            userperson.quanity1 = number
            userperson.save()

        if "jordan3" in resultlist:
            productobj = Items.objects.get(id=4)
            userperson.item.add(productobj)
            number = int(request.POST["jordan3"])
            userperson.quanity4 = number
            userperson.save()

        if "jordan4" in resultlist:
            productobj = Items.objects.get(id=3)
            userperson.item.add(productobj)
            number = int(request.POST["jordan4"])
            userperson.quanity3 = number
            userperson.save()
    allitems = userperson.item.all()
    context = {"allitems": allitems,
               "one": userperson.quanity1,
               "two": userperson.quanity2,
               "three": userperson.quanity3,
               "four": userperson.quanity4}
    return render(request, 'shippinginfo.html', context)

def final(request):
    personName=request.POST["name"]
    email = request.POST["email"]
    address = request.POST["address"]
    zipcode = request.POST["zipcode"]
    state = request.POST["state"]

    currentip = get_client_ip(request)[0]
    userperson = user.objects.get_or_create(ipaddress=currentip)
    userperson = userperson[0]
    if request.method=='POST':
       obj=shipping_info.objects.create(name=personName,
                                    email=email,
                                   zipcode=zipcode,
                                    address=address,
                                   citystate=state)
    context={"username":obj.name,
             "email": obj.email,
             "zipcode": obj.zipcode,
             "address": obj.address,
             "citystate": state}

    return render(request, 'final.html', context)


def delete(request, pk):
    deleteitem=Items.objects.get(id=pk)
    currentip = get_client_ip(request)[0]
    userperson = user.objects.get_or_create(ipaddress=currentip)
    userperson = userperson[0]
    userperson.item.remove(deleteitem)
    next = request.META.get('HTTP_REFERER', None) or '/'
    return HttpResponseRedirect(next)