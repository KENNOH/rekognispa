from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

UserProfile = get_user_model()


class UserProfileCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'email')


class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'email')
