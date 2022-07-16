
from turtle import home
from xml.sax.handler import property_declaration_handler
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads"))
]
