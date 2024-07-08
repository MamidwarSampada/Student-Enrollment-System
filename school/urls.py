
from django.contrib import admin
from django.urls import path
from student import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.show),
    path('register/', views.register),
    path('existing/', views.existing),
     path('search/', views.search),
     path('drop/', views.droupout),
]
