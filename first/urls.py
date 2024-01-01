from django.urls import path

from first.views import first


urlpatterns = [
    path("first/", view=first, name="first")
]
