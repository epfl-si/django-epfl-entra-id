import jwt
from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from mozilla_django_oidc.auth import OIDCAuthenticationBackend

User = get_user_model()


class EPFLOIDCAB(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user = self.update_attributes_if_same_sciper(claims)
        if user:
            return user

        user = User.objects.create_user(
            username=claims.get("gaspar"),
            email=claims.get("email"),
            first_name=claims.get("given_name"),
            last_name=claims.get("family_name"),
        )

        model_path = settings.USER_PROFILE_MODEL
        ProfileModel = apps.get_model(*model_path.split("."))
        profile, _ = ProfileModel.objects.get_or_create(user=user)
        profile.sciper = claims.get("uniqueid")
        profile.save()

        return user

    def update_user(self, user, claims):
        user.username = claims.get("gaspar")
        user.email = claims.get("email")
        user.first_name = claims.get("given_name")
        user.last_name = claims.get("family_name")
        user.save()

        user.profile.sciper = claims.get("uniqueid")
        user.profile.save()

        return user

    def get_userinfo(self, access_token, id_token, payload):
        """
        Get user info from both user info endpoint (default) and
        merge with ID token information.
        """
        userinfo = super(EPFLOIDCAB, self).get_userinfo(
            access_token, id_token, payload
        )

        id_token_decoded: str = jwt.decode(
            id_token, options={"verify_signature": False}
        )

        userinfo.update(id_token_decoded)

        return userinfo

    def update_attributes_if_same_sciper(self, claims):
        profile = self.get_user_profile(sciper=claims.get("uniqueid"))

        print(profile)

        if profile is None:
            return None

        updated = False
        if profile.user.username != claims.get("gaspar"):
            profile.user.username = claims.get("gaspar")
            updated = True
        if profile.user.email != claims.get("email"):
            profile.user.email = claims.get("email")
            updated = True
        if profile.user.first_name != claims.get("given_name"):
            profile.user.first_name = claims.get("given_name")
            updated = True
        if profile.user.last_name != claims.get("family_name"):
            profile.user.last_name = claims.get("family_name")
            updated = True

        if updated:
            profile.user.save()

        return profile.user

    def get_user_profile(self, sciper):
        model_path = settings.USER_PROFILE_MODEL
        ProfileModel = apps.get_model(*model_path.split("."))
        return ProfileModel.objects.filter(sciper=sciper).first()
