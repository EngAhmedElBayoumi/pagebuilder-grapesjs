from . import views
from django.urls import path

app_name = "pages"

urlpatterns = [
    path("en/<slug:slug>/", views.index_en, name="pages"),
    path("<slug:slug>/", views.index, name="pages"),
    path('', views.home, name="home"),
]