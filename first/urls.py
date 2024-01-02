from django.urls import path

from first.views import first, thankyou


urlpatterns = [
    path("first/", view=first, name="first"),
    path("success/", view=thankyou)
]
