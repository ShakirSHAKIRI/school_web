
from django.urls import path
from .views import Home,Add_Section

urlpatterns = [
    path('',Home),
    path('add_section',Add_Section,name='add_section')
]
