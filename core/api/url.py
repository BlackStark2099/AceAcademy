import home.views as view
from django.urls import path

urlpatterns = [
    path("index/", view.first_api),
    path('getperson/',view.get_persons),
    path('addperson/',view.add_person)
]