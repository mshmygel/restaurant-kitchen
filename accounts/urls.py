from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import (
    CookListView,
    CookDetailView,
    CookCreateView,
    CookExperienceUpdateView,
    CookDeleteView
)

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login"
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="registration/logged_out.html"),
        name="logout"
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path("cooks/create/",
         CookCreateView.as_view(),
         name="cook-create"
         ),
    path(
        "cooks/<int:pk>/update/",
        CookExperienceUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),
]
