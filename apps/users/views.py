from django.contrib.auth.models import Group,User
from rest_framework import viewsets

from users.models import UserProfile
from users.serializers import UserSerializer, GroupSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get(self):
        self.dispatch()
