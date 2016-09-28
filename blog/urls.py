from django.conf.urls import include, url
from blog import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail')
]
