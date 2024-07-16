from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import kitchen_login
from user.models import Order,OrderItem
# Create your views here.


def kitchen_log(request):

    if "kitchen_username" in request.session:
        return redirect('kitchen_home')
    if request.method =="POST":

        username=request.POST['username']
        password=request.POST['password']

        kitchen=kitchen_login.objects.filter(username=username,password=password).first()

        if kitchen is not None:
            request.session['kitchen_username']= username
            return JsonResponse({'success':True}, safe=False)
        else:
            return JsonResponse({'success':False},safe=False)
        
    return render(request,"kitchen/kitchen_login.html")


def kitchen_logout(request):
    if 'kitchen_username' in request.session:
        request.session.flush()
    return redirect('home')


def kitchen_home(request):
    orders=Order.objects.filter(approve=True)
    context={'orders':orders}
    return render(request,"kitchen/kitchenhome.html",context)


def view_request(request,req_id):
    try:
        order= Order.objects.get(pk=req_id)
        bill= OrderItem.objects.filter(order=order)
    except Order.DoesNotExist:
        return redirect('kitchen_home') 
    context={'order':order,'bill':bill}
    return render(request,"kitchen/viewrequest.html",context)