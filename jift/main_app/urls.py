from django.urls import path

from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
    path('item/<int:item_id>/', views.item, name='item'),
]
