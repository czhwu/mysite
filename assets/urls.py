from django.conf.urls import url
from assets import views

urlpatterns = [
    url(r'^$', views.detail, name='detail')
]