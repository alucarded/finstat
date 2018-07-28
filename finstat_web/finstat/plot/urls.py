from django.conf.urls import url

from . import views

urlpatterns = [
    # /finstat
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^chart/$', views.PlotView.as_view(), name='chart'),
]
