from django.test import TestCase
from django.contrib.auth import get_user_model

	def test_create_user_with_email_sucessfull(self):

		 email =  'test@londonappdev.com'
		 password = "Testpass123"
		 user = get_user_model().objects.create_user(email=email, password=password)


		 self.assertEqual(user.email, email)
		 self.assertTrue(user.check_password(password))