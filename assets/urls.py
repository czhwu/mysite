from django.conf.urls import url
from assets import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^(?P<gdzc>\w+)/$', views.detail, name='detail'),
]
