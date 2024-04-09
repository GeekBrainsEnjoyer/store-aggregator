from django.shortcuts import render

from item.models import Category, Item


def index(request):
    item_set = Item.objects.all()
    category_set = Category.objects.all()
    return render(request, 'core/index.html',
                  {
                      'category_set': category_set,
                      'item_set': item_set,
                  })
