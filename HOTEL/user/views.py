from django.shortcuts import render,redirect
from .models import Order,OrderItem,TABLE_CHOICES
from base.models import Today_item
from django.http import JsonResponse

#Create your views here.



def order_item(request):
    today_items = Today_item.objects.all()
    
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        table = request.POST.get('table')
        
        # Check if the selected table is already occupied
        if Order.objects.filter(table=table, approve=True).exists():
            return JsonResponse({'success': False, 'message': 'Selected table is currently occupied.'})
        
        order = Order.objects.create(table=table, approve=True)
        
        for item_id, quantity in request.POST.items():
            if item_id.startswith('item_'):
                item_id = item_id.split('_')[1]
                today_item = Today_item.objects.get(id=item_id)
                OrderItem.objects.create(order=order, item=today_item.add_item, quantity=quantity)
        
        return JsonResponse({'success': True, 'message': 'Order placed successfully!'})

    context = {'today_items': today_items, 'TABLE_CHOICES': TABLE_CHOICES}
    return render(request, 'user/orderfood.html', context)



def menu(request):
    menu=Today_item.objects.all()
    context={'menu':menu}
    return render(request,"user/viewmenu.html",context)




