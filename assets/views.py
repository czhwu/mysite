from django.shortcuts import render
from . import models


# Create your views here.
def detail(request):
    assets_list = models.AssetDetail.objects.order_by('dpt')
    context = {"assets_list": assets_list}
    return render(request, 'assets/detail.html', context)
