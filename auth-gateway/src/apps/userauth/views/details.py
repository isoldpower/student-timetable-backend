from dj_rest_auth.serializers import UserDetailsSerializer

class CustomUserDetailsSerializer(UserDetailsSerializer):
    username = None

    class Meta(UserDetailsSerializer.Meta):
        fields = ('pk', 'email', 'first_name', 'last_name')