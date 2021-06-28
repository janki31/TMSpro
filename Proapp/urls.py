from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.home,name="homepage"),
    path('',views.index,name="homepage"),
    path('contact/',views.contact,name="contact"),
    path('poojabooking/',views.poojabooking,name="poojabooking"),
    path('basic/',views.basic,name="basic"),
    path('imagegallery/',views.imagegallery,name="imagegallery"),
    path('about/',views.about,name="about"),
    path('facilities/',views.facilities,name="facilities"),
    path('funddonation/',views.funddonation,name="funddonation"),
    path('blooddonation/',views.blooddonation,name="blooddonation"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    #path('payment/',views.payment,name="payment"),


]
