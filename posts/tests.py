from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='test_user', password='abc123')
        test_user.save()

        test_post = Post.objects.create(
            author=test_user, title='Blog Title', body='Body Content...')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'test_user')
        self.assertEqual(title, 'Blog Title')
        self.assertEqual(body, 'Body Content...')
