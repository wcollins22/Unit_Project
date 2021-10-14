from django.contrib import admin
from django.urls import path
import app.views
from app.views import profile_function, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", app.views.profile_function, name="pf"),
    path("home2/", app.views.home_view, name="home"),
    path("student/<name>/", app.views.student_view, name="student") 
]
