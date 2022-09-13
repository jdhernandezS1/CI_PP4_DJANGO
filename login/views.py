from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
# Create your views here.


def login_fc(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'login/login.html', context)


def register_fc(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_fc')
    form =  ItemForm()
    context = {
        'form': form
    }
    return render(request, 'login/register.html', context)

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('login_fc')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'login/edit_item.html',context)