from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q

from .models import Item, Category
from .forms import ItemForm, EditItemForm


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/detail.html', {
        'item': item, })


def browse(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    item_set = Item.objects.filter(is_sold=False)
    category_set = Category.objects.all()

    if category_id:
        item_set = item_set.filter(category_id=category_id)

    if query:
        item_set = item_set.filter(Q(name__icontains=query) |
                                   Q(description__icontains=query))

    return render(request, 'item/browse.html',
                  {
                      'title': 'Browse',
                      'category_set': category_set,
                      'item_set': item_set,
                      'category_id': int(category_id)
                  })


@login_required
def new_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)

    else:
        form = ItemForm()

    return render(request, 'item/item_form.html', {'form': form, 'title': 'New item'})


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)

    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/item_form.html', {'form': form, 'title': 'Edit item'})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')
