from django.urls import path
from . import views

urlpatterns = [
    path("points-submitting/<int:pk>/", views.SubmissionPointsView.as_view(), name="add-points"),
    path("ranking/", views.RankingView.as_view(), name="ranking")
]
