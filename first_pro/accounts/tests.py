from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user_hashes_password(self):
        user = get_user_model().objects.create_user(
            username='backend-reviewer',
            password='test-password',
        )

        self.assertEqual(user.username, 'backend-reviewer')
        self.assertTrue(user.check_password('test-password'))
