from django.urls import path
from .views import SearchResultView, CarDetailView, FilterResultView , HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("result", SearchResultView.as_view(), name="search_results"),
    path("filter", FilterResultView.as_view(), name="filter_results"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
]