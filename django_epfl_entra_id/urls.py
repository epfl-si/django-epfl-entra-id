from django.urls import path

from django_epfl_entra_id import views

urlpatterns = [
    path(
        "admin/login/",
        views.EPFLEntraIdLogin.as_view(),
        name="epfl_entra_id_init",
    ),
]
