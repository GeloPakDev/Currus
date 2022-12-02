from django.urls import path
from .views import HomePageView, SearchResultPage

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("result", SearchResultPage.as_view(), name="result")
]
