

from django.contrib import admin
from django.urls import path
import app.views
from app.views import profile_function

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", app.views.profile_function, name="pf")
]
