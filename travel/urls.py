from django.urls import path
from .views import KlassView, MehmonxonaView, TravelView


urlpatterns = [
    path("klass/", KlassView.as_view()),
    path("klass/<int:pk>/", KlassView.as_view()),
    path("mehmonxona/", MehmonxonaView.as_view()),
    path("travel/", TravelView.as_view()),
]