from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from item.models import Item


@login_required
def index(request):
    item_set = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {'item_set': item_set})
