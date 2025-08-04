from django.urls import include, path, re_path

urlpatterns = [
    re_path(r"^auth/", include("mozilla_django_oidc.urls")),
    path("", include("django_epfl_entra_id.urls")),
]
