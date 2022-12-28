from .views import *
from django.urls import path

urlpatterns = [
    path("", HomeView.as_view(),name = "home"),
    path("category/<slug>", CategoryView.as_view(),name = "category"),
    path("search", SearchView.as_view(),name = "search"),
    path("details/<slug>", ProductDetailView.as_view(),name = "details"),
]