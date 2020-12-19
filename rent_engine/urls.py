from django.urls import path

from rent_engine.views import BookRentAPI

app_name = "rent_engine"
urlpatterns = [
    path('v1/', BookRentAPI.as_view(), name="user-books"),
]