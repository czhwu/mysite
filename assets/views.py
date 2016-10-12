from django.shortcuts import render
from . import models


# Create your views here.
def list(request):
    assets_list = models.AssetDetail.objects.order_by('dpt')
    context = {"assets_list": assets_list}
    return render(request, 'assets/list.html', context)


def detail(request, gdzc):
    asset = models.AssetDetail.objects.get(gdzc=gdzc)
    context = {'asset': asset}
    return render(request, 'assets/detail.html', context)
