from django.conf.urls import url

from . import views # import views so we can use them in urls.

app_name='product'

urlpatterns = [
    url(r'^$', views.search_results),
    
]