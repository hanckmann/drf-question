from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.urls import reverse

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse

from rest_framework.test import APIClient
import factory

from .factories import UserFactory
from api.accounts.serializers import UserSerializer


User = get_user_model()

USERS_LIST = reverse('user-list')


class TestUserSerializers(TestCase):

    @factory.django.mute_signals(post_save)
    def setUp(self):
        self.user = UserFactory(username="user", email="user@example.com")
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    @factory.django.mute_signals(post_save)
    def test_retrieve_user_list(self):
        User.objects.create(email='test1@voorbeeld.nl')
        User.objects.create(email='test2@example.com')
        User.objects.create(email='test3@ejemplo.es')
        result = self.client.get(USERS_LIST)
        users = User.objects.all().order_by('-id')
        serializer = UserSerializer(users, many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data, serializer.data)
