
from django.urls import path, include
from .views import (
  TeamApiView,
)

urlpatterns = [
  path('team/<int:team_id>/', TeamApiView.as_view())
]