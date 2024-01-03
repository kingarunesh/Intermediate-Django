from django.urls import path

from second.views import second


urlpatterns = [
    path("second/", view=second, name="second")
]
