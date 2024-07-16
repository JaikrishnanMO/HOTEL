from django.shortcuts import get_object_or_404, render,redirect
from .models import Admin_model,Add_item,Today_item
from user.models import Order,OrderItem
from django.http import JsonResponse
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request,'base/home.html')


def admin_login(request):
    if "admin_username" in request.session:
        return redirect('Admin_home')
    if request.method =="POST":

        username=request.POST['username']
        password=request.POST['password']

        admin=Admin_model.objects.filter(username=username,password=password).first()

        if admin is not None:
            request.session['admin_username']= username
            return JsonResponse({'success':True}, safe=False)
        else:
            return JsonResponse({'success':False},safe=False)
        
    return render(request,"base/adminlogin.html")

def Admin_home(request):
    return render(request,"base/adminhome.html")

def Add_food(request):
    if request.method == "POST":
        item_name=request.POST['itemname']
        price=request.POST['price']
        description=request.POST['details']

        if not item_name or not price or not description:
            return JsonResponse({'success': False, 'message': 'All fields are required.'})
        
        try:
            price = float(price) 
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Price must be a valid number.'})



        if Add_item.objects.filter(item_name=item_name, price=price, description=description).exists():
                return JsonResponse({'success': False, 'message': 'Item already exists.'})

    
        new_food = Add_item(item_name=item_name, price=price, description=description)
        new_food.save()
        
        return JsonResponse({'success': True, 'message': 'Item added successfully.'})

    return render(request,"base/addfood.html") 



def view_food(request):
    food= Add_item.objects.all()
    context={'food':food}
    return render(request,"base/viewfood.html",context)


def update_food(request,item_id):
    food_item=Add_item.objects.get(pk=item_id)

    if request.method == 'POST':

        food_item.item_name= request.POST.get('item_name')
        food_item.price=request.POST.get('price')
        food_item.description=request.POST.get('description')

        food_item.save()
        return redirect('view_food')
    return render(request,"base/updatefood.html",{'food_item':food_item})




def delete_food(request,item_id):
    food_item = Add_item.objects.get(pk=item_id)

    if request.method == "POST":
        food_item.delete()
        return redirect('view_food')
    return render(request,"base/deletefood.html",{'food_item':food_item})



def today_menu(request):
    food_items = Add_item.objects.all()
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        add_item = Add_item.objects.get(item_name=item_name)
        today_exists = Today_item.objects.filter(add_item=add_item, created_at__date=timezone.now().date()).exists()

        if not today_exists:
            today_item = Today_item(add_item=add_item)
            today_item.save()
            return JsonResponse({'success': True, 'message': 'Item added successfully.'})
        else:
            return JsonResponse({'success': False, 'message': 'Item already added today.'})

    context = {'food_items': food_items}
    return render(request, "base/todaymenu.html", context)


def view_today_menu(request):
    today_menu = Today_item.objects.all()
    context={'today_menu': today_menu}
    return render(request,"base/viewtodaymenu.html",context)


def delete_today_menu(request,item_id):
    food_item=Today_item.objects.get(pk=item_id)

    if request.method == 'POST':

        food_item.delete()
        return redirect('view_today_menu')
    return render(request,"base/deletetodaymenu.html",{'food_item':food_item})


def view_orders(request):
    orders=Order.objects.filter(approve=True)
    context={'orders':orders}
    return render(request,"base/vieworder.html",context)


def view_order_item(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        bill = OrderItem.objects.filter(order=order)
    except Order.DoesNotExist:
        return redirect('order_list')

    # Calculate the grand total
    grand_total = sum(item.total_price for item in bill if item.total_price > 0)

    context = {
        'order': order,
        'bill': bill,
        'grand_total': grand_total,
    }
    return render(request, "base/viewbill.html", context)

def accept_payment(request, food_id):
    try:
        order = Order.objects.get(pk=food_id)
        order.approve = False
        order.save()
        return redirect('view_orders')  # Redirect to the view_orders page after payment acceptance
    except Order.DoesNotExist:
        # Handle the case where Order with food_id does not exist
        return redirect('view_orders') 

def admin_logout(request):
    if 'admin_username' in request.session:
        request.session.flush()
    return redirect('home')