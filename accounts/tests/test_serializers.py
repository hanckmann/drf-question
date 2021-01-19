from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.request import Request

from rest_framework.test import APIClient, APIRequestFactory
import factory

from accounts.serializers import UserSerializer
from .factories import UserFactory


User = get_user_model()

USERS_LIST = reverse('user-list')


class TestUserSerializers(TestCase):

    @factory.django.mute_signals(post_save)
    def setUp(self):
        self.user = UserFactory(username="user", email="user@example.com")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        factory = APIRequestFactory()
        request = factory.get('/')
        self.serializer_context = {
            'request': Request(request),
        }

    @factory.django.mute_signals(post_save)
    def test_retrieve_user_list(self):
        User.objects.create(username='test1', email='test1@voorbeeld.nl')
        User.objects.create(username='test2', email='test2@example.com')
        User.objects.create(username='test3', email='test3@ejemplo.es')
        result = self.client.get(USERS_LIST)
        users = User.objects.all().order_by('-id')
        serializer = UserSerializer(users, context=self.serializer_context, many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['results'], serializer.data)
