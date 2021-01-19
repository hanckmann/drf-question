from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
import factory

from .factories import UserFactory


User = get_user_model()

USERS_URL = reverse('user-list')


class TestUserModel(TestCase):

    @factory.django.mute_signals(post_save)
    def setUp(self):
        self.user = UserFactory(username='test1', email="test1@test.nl")
        self.superuser = UserFactory(username='test2', email="test2@test.nl")
        self.superuser.is_staff = True
        self.superuser.is_superuser = True
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.client.force_authenticate(self.superuser)

    # @factory.django.mute_signals(post_save)
    # def test__user_str_representation_to_be_email(self):
    #     self.assertEqual(str(self.user), self.user.email)

    def test_post_user_successful(self):
        payload = {
            'email': 'test3@test.nl',
            'username': 'test3',
            'name': 'Full name'
        }
        ret = self.client.post(USERS_URL, payload)
        exists = User.objects.filter(
            email=payload['email']
        ).exists()
        self.assertEqual(ret.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertFalse(exists)

    @factory.django.mute_signals(post_save)
    def test_user_permissions(self):
        self.assertEqual(self.user.is_staff, False)
        self.assertEqual(self.user.is_superuser, False)

    @factory.django.mute_signals(post_save)
    def test_superuser_permissions(self):
        self.assertEqual(self.superuser.is_staff, True)
        self.assertEqual(self.superuser.is_superuser, True)
