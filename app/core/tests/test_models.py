from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'kiarashtestcase123123@kiarash.men'
        password = 'TEST@$^T$#%RFfs21234'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'kiarashtestcase123123@KIARASH.MEN'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser('test1232313userpuser@kiarash.men', 'asdasd@!#@RFDSDas123434')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
