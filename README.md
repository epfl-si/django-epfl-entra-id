# django-epfl-entra-id

[Entra ID](https://inside.epfl.ch/identite-numerique/) authentication for Django.


Requirements
============

``django-epfl-entra-id`` needs Django 3.2+ LTS

Installation
============

```bash
pip install git+https://github.com/epfl-si/django-epfl-entra-id.git
```

Configuration
=============

settings.py
-----------

* Add in your ``MIDDLEWARE``:
```bash
MIDDLEWARE = [
  ...
  'login_required.middleware.LoginRequiredMiddleware',
  ...
 ]
```

* Add into ``INSTALLED_APPS``:
```bash
INSTALLED_APPS = [
  ...
  'django.contrib.auth',
  'mozilla_django_oidc',
  ...
]
```

* Add to authentication backends:
```bash
USER_PROFILE_MODEL = "userprofile.UserProfile" # or your user model

AUTHENTICATION_BACKENDS = ("django_epfl_entra_id.backend.OFRFOIDCAB", "django.contrib.auth.backends.ModelBackend")
```

* Add OIDC configuration:
```bash
TENANT_ID = os.environ["TENANT_ID"]

OIDC_RP_CLIENT_ID = os.environ["OIDC_RP_CLIENT_ID"]
OIDC_RP_CLIENT_SECRET = os.environ["OIDC_RP_CLIENT_SECRET"]

AUTH_DOMAIN = f"https://login.microsoftonline.com/{TENANT_ID}"
OIDC_OP_AUTHORIZATION_ENDPOINT = f"{AUTH_DOMAIN}/oauth2/v2.0/authorize"
OIDC_OP_TOKEN_ENDPOINT = f"{AUTH_DOMAIN}/oauth2/v2.0/token"
OIDC_OP_JWKS_ENDPOINT = f"{AUTH_DOMAIN}/discovery/v2.0/keys"
OIDC_OP_USER_ENDPOINT = "https://graph.microsoft.com/oidc/userinfo"
OIDC_RP_SIGN_ALGO = "RS256"

LOGIN_URL = '/oidc/authenticate'
LOGIN_REDIRECT_URL = "/homepage"
LOGOUT_REDIRECT_URL = "/"

# Only use this setting if you want to store the access token in the session
# To use access token to call API
OIDC_STORE_ACCESS_TOKEN = True
```

* Configure required ignore paths
```bash
LOGIN_REQUIRED_IGNORE_PATHS = [
  r'/accounts/login/$',
  r'/accounts/logout/$',
  r'^/oidc/.*$',  # All OIDC-related URLs
  r'^/admin/.*$',
  r'^/admin$',
  r'^/static/.*$',
  r'^/media/.*$',
]
```

urls.py
-------

* Add these lines:
```bash
urlpatterns += re_path(r'^oidc/', include('mozilla_django_oidc.urls')),
```

\(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, DSI
