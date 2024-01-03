from django.urls import path, register_converter

from third.views import third_view, hello, second_view, student_view, teacher_view
from third.converters import FourDigitYearConverter


register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("", view=third_view, name="third"),
    
    path("hello/<first_id>/<int:second_id>/<slug:my_slug>/<yyyy:year>/", view=hello, kwargs={"check": "Yes"}, name="hello"),
    
    path("second/", view=second_view, name="second"),
    
    path("student/", view=student_view),
    
    path("teacher/", view=teacher_view, name="teacher")
]
