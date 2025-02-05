from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path("contact/",views.contact),
    path("about/",views.about),
    path("pictures/",views.pictures),
    path("amenities/",views.amenities),
    path("booknow/",views.booknow),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
