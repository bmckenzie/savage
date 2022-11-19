from django.test import TestCase
from users.models import User

# Create your tests here.


class UserTestCase(TestCase):
  def setUp(self):
    User.objects.create(username='John Doe', email='john@example.com',)

  def test_locate_user_by_email(self):
    user = User.objects.get(email="john@example.com")
    self.assertEqual(user.email, "john@example.com")

  def set_description(self):
    user = User.objects.get(email="john@example.com")
    user.set_description("This is a description.")
    self.assertEqual(user.description, "This is a description.")