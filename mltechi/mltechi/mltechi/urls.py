"""
mltechi URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from landing import views as landing_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_views.home, name='landing-home'),
]
