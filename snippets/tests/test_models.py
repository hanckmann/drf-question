from django.db.models.signals import post_save
from rest_framework import status
from rest_framework.reverse import reverse

from django.test import TestCase
from rest_framework.test import APIClient
import factory

from accounts.tests.factories import UserFactory
from snippets.models import Snippet


SNIPPETS_URL = reverse('snippet-list')


class TestSnippetModel(TestCase):

    @factory.django.mute_signals(post_save)
    def setUp(self):
        self.user = UserFactory(email='user@example.com')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_create_snippet_successful(self):
        payload = {
            'title': 'TITLE1',
            'code': 'CODE ONE',
            'linenos': False,
            'language': 'Erlang',
            'style': None
        }
        self.client.post(SNIPPETS_URL, payload)
        exists = Snippet.objects.filter(
            owner=self.user
        ).exists()
        self.assertTrue(exists)
        self.client.post(SNIPPETS_URL, payload)
        result = Snippet.objects.filter(
            owner=self.user
        ).all()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, 'TITLE1')
        self.assertEqual(result[0].code, 'CODE ONE')
        self.assertEqual(result[0].style, None)
