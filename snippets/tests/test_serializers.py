from django.db.models.signals import post_save
from rest_framework import status
from rest_framework.reverse import reverse

from django.test import TestCase
from rest_framework.test import APIClient
import factory

from accounts.tests.factories import UserFactory
from snippets.serializers import SnippetSerializer
from snippets.models import Snippet


SNIPPETS_URL = reverse('snippet-list')


class TestSnippetSerializer(TestCase):

    @factory.django.mute_signals(post_save)
    def setUp(self):
        self.user = UserFactory(email="user@example.com")
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    @factory.django.mute_signals(post_save)
    def test_retrieve_snippet_list(self):
        Snippet.objects.create(title='snip 1')
        Snippet.objects.create(title='snip 2', code='some code;')
        Snippet.objects.create(title='snip 3', code='more code;', language='Python')
        result = self.client.get(SNIPPETS_URL)
        snippets = Snippet.objects.all().order_by('-id')
        serializer = SnippetSerializer(snippets, many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data, serializer.data)
        print(SNIPPETS_URL)
        print(result.data)
        print(serializer.data)

    @factory.django.mute_signals(post_save)
    def test_create_ingredient_successful(self):
        payload = {
            'title': 'snip 0',
            'code': 'source code;',
            'language': 'C++'
        }
        self.client.post(SNIPPETS_URL, payload)
        exists = Snippet.objects.filter(
            user=self.user,
            name=payload['name'],
        ).exists()
        snippets = Snippet.objects.filter(
            user=self.user,
            name=payload['name'],
        ).all()
        self.assertTrue(exists)
        self.assertEqual(len(snippets), 1)
        self.assertEqual(snippets[0].title, payload['title'])
        self.assertEqual(snippets[0].code, payload['code'])
        self.assertEqual(snippets[0].language, payload['language'])
        self.assertEqual(snippets[0].owner, self.user)
