from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
import factory

from .factories import UserFactory


User = get_user_model()

USERS_URL = reverse('snippet-list')


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

    # def test_get_user_successful(self):
    #     # payload = {
    #     #     'email': 'test3@test.nl',
    #     #     'username': 'test3',
    #     #     'name': 'Full name'
    #     # }
    #     # self.client.post(USERS_URL, payload)
    #     # exists = User.objects.filter(
    #     #     username=self.user.username
    #     # ).exists()
    #     # self.assertTrue(exists)

    #     self.assertEqualself.user
    #     self.assertEqualself.superuser

    #     self.assertEqual(len(result), 1)
    #     self.assertEqual(result[0].title, 'TITLE1')
    #     self.assertEqual(result[0].code, 'CODE ONE')
    #     self.assertEqual(result[0].style, None)

    @factory.django.mute_signals(post_save)
    def test_user_permissions(self):
        self.assertEqual(self.user.is_staff, False)
        self.assertEqual(self.user.is_superuser, False)

    @factory.django.mute_signals(post_save)
    def test_superuser_permissions(self):
        self.assertEqual(self.superuser.is_staff, True)
        self.assertEqual(self.superuser.is_superuser, True)
