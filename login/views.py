from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
<<<<<<< HEAD
from django.views.generic import ListView
=======
>>>>>>> parent of 71d36b1 (config view Boostrap)
from .models import Item
from .forms import ItemForm
# Create your views here.


<<<<<<< HEAD
class PostList(ListView):
    model = Item
    queryset = Item.objects.filter(status=1).order_by('-created_on')
    template_name = index.html
    paginate_by = 6


=======
>>>>>>> parent of 71d36b1 (config view Boostrap)
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