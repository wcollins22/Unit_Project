from django.contrib import admin
from django.urls import path
import app.views
from app.views import page_view, profile_function, home_view, homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("profile/", app.views.profile_function, name="pf"),
    path("person/<u_name>/", app.views.page_view, name="person"),
    path("home/", app.views.home_view, name="home"),
    path("homepage/", app.views.homepage, name="hpnew")
]
