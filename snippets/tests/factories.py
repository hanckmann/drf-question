import factory
from factory import fuzzy

from django.contrib.auth import get_user_model


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: "user{0}@example.com".format(n))
    email = factory.Sequence(lambda n: "user{0}@example.com".format(n))
    password = factory.PostGenerationMethodCall("set_password", "password")
    is_verified = fuzzy.FuzzyChoice([True, False])

    class Meta:
        model = "accounts.User"
        django_get_or_create = ["email"]

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = 'john'