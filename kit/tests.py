from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Kit

# Create your tests here.

class KitTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_kit = Kit.objects.create(
            author = testuser1,
            name = 'Green Eggs and Ham',
            review = 'I do not like green eggs and ham, Sam I  am.'
        )
        test_kit.save()

    def test_kit_content(self):
        kit = Kit.objects.get(id=1)
        actual_author = str(kit.author)
        actual_name = str(kit.name)
        actual_review = str(kit.review)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_name, 'Green Eggs and Ham')
        self.assertEqual(actual_review, 'I do not like green eggs and ham, Sam I  am.')