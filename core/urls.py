from django.urls import path

from .views import FootballerDeleteView
from .views import FootballerListCreateView


urlpatterns = [
    path('footballers', FootballerListCreateView.as_view()),
    path('footballers/<int:pk>/delete', FootballerDeleteView.as_view())
]
