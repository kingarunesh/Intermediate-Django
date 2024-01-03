from django.urls import path

from third.views import third_view


urlpatterns = [
    path("", view=third_view, name="third")
]
