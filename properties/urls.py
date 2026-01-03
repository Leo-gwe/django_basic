from django.urls import path
from . import views


urlpatterns = [
    path('<int:property_id>/', views.property_detail, name='property_detail'),
]