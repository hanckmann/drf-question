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
        self.user = UserFactory(username='test', email='user@example.com')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    @factory.django.mute_signals(post_save)
    def test_create_snippet_successful(self):
        print(SNIPPETS_URL)
        payload = {
            'title': 'TITLE1',
            'code': 'CODE ONE',
            'linenos': False,
            'language': 'erlang',
        }
        ret = self.client.post(SNIPPETS_URL, payload)
        exists = Snippet.objects.filter(
            owner=self.user
        ).exists()
        self.client.post(SNIPPETS_URL, payload)
        result = Snippet.objects.filter(
            owner=self.user
        ).all()
        self.assertEqual(ret.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)
        self.assertEqual(result[0].title, payload['title'])
        self.assertEqual(result[0].code, payload['code'])
        self.assertEqual(result[0].language, payload['language'])
