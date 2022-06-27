
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.home, name="home"),
    path ('about-me/', views.about, name="about"),
    path ('portfolio/', views.portfolio, name="portfolio"),
    path ('contact/', views.contact, name="contact"),
]
