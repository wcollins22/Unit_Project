from django.contrib import admin
from django.urls import path
import app.views
from app.views import profile_function, homepage_view, page_view

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("profile/", app.views.profile_function, name="pf"),
<<<<<<< HEAD
    path("person/<u_name>/", app.views.page_view, name="person"),
    path("home/", app.views.home_view, name="home"),
    
=======
    path("homepage/", app.views.homepage_view, name="hpnew"),
    path("homepage/<name>/", app.views.page_view, name="page")
>>>>>>> 33583434129e181da1c65ed0820a13be925c450a
]
urlpatterns += staticfiles_urlpatterns()
