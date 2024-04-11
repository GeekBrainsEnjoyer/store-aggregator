from django.shortcuts import render, redirect

from item.models import Category, Item
from .forms import SignupForm


def index(request):
    item_set = Item.objects.all()
    category_set = Category.objects.all()
    return render(request, 'core/index.html',
                  {
                      'category_set': category_set,
                      'item_set': item_set,
                  })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})
