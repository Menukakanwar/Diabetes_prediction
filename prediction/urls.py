from django.contrib import admin
from django.urls import path
from prediction import views
urlpatterns=[
    path('prediction/',views.home),
    path('admin/', admin.site.urls),
]