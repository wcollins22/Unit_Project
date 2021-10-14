from django.contrib import admin
from django.urls import path
import app.views
from app.views import profile_function, homepage_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("profile/", app.views.profile_function, name="pf"),
    path("homepage/", app.views.homepage_view, name="hpnew")
]
