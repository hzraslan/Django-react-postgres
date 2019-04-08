from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.getall),
    url(r'^main$', views.main),
]