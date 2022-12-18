from django.urls import path
from .views import SearchResultView, CarDetailView, FilterResultView, HomePageView, FullSearchView, AdvancedSearchView, \
    CategoryFilterView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("result", SearchResultView.as_view(), name="search_results"),
    path("filter", FilterResultView.as_view(), name="filter_results"),
    path("category", CategoryFilterView.as_view(), name="category_filter"),
    path("full_filter", FullSearchView.as_view(), name="full_filter_results"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
    path("advanced_search", AdvancedSearchView.as_view(), name="advanced_search"),
]
