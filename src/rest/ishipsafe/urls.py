from django.conf.urls import url
from ishipsafe import views 	

urlpatterns = [
    url(r'^ishipsafe/$', views.snippet_list),
    url(r'^ishipsafe/getpricing/$', views.pricelisting_detail),
]
