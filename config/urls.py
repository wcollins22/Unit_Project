from django.contrib import admin
from django.urls import path
import app.views
from app.views import profile_function, homepage_view, page_view

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("profile/", app.views.profile_function, name="pf"),
<<<<<<< Updated upstream
    path("person/<name>/", app.views.page_view, name="person"),
    path("homepage/", app.views.homepage_view, name="home"),
=======
    path("homepage/<name>/", app.views.page_view, name="person"),
    path("home/", app.views.homepage_view, name="hpnew"),
>>>>>>> Stashed changes
    
]
urlpatterns += staticfiles_urlpatterns()
