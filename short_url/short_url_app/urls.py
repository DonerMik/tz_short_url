from django.urls import path

from short_url_app import views

app_name = 'short_url'

urlpatterns = [
    path('<str:slug>/', views.redirect_url, name='link_redirect'),
    path('generate_url', views.generate_url, name='generate_url'),
    path('list_url', views.get_list_url, name='list_url'),
    path('', views.index, name='index'),
    ]
