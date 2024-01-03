
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("first.urls")),
    path("", include("second.urls")),
    path("third/", include("third.urls"))
]
