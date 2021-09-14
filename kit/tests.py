from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Kit

# Create your tests here.

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_post = Kit.objects.create(
            author = testuser1,
            name = 'Green Eggs and Ham',
            review = 'I do not like green eggs and ham, Sam I  am.'
        )
        test_post.save()

    def test_blog_content(self):
        post = Kit.objects.get(id=1)
        actual_author = str(post.author)
        actual_name = str(post.name)
        actual_review = str(post.review)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_name, 'Green Eggs and Ham')
        self.assertEqual(actual_review, 'I do not like green eggs and ham, Sam I  am.')