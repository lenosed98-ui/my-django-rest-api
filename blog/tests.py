from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

class PostModelTest(TestCase):
    def test_create_post(self):
        user = User.objects.create_user('u', 'u@x.com', 'pass12345')
        cat = Category.objects.create(name='Tech')
        post = Post.objects.create(author=user, category=cat, title='T', content='C')
        self.assertEqual(str(post.title), 'T')
