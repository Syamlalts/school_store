from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.person_create_view, name='add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    # path('form', views.form, name='form'),
    path('confirm', views.confirm, name='confirm'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    # AJAX
]