import unittest
from user_registration import UserRegistration

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.user = UserRegistration()

    def test_valid_emails(self):
        valid_emails = [
            "user@example.com",
            "test.user@gmail.com",
            "abc123@yahoo.in"
        ]
        for email in valid_emails:
            self.assertTrue(self.user.validate_email(email))

    def test_invalid_emails(self):
        invalid_emails = [
            "userexample.com",
            "user@com",
            "@gmail.com",
            "user@gmail"
        ]
        for email in invalid_emails:
            self.assertFalse(self.user.validate_email(email))

    def test_valid_passwords(self):
        valid_passwords = [
            "Password@123",
            "Abc@1234",
            "Test@2024"
        ]
        for pwd in valid_passwords:
            self.assertTrue(self.user.validate_password(pwd))

    def test_invalid_passwords(self):
        invalid_passwords = [
            "password",
            "PASS1234",
            "Pass@12",
            "Password123"
        ]
        for pwd in invalid_passwords:
            self.assertFalse(self.user.validate_password(pwd))

if __name__ == "__main__":
    unittest.main()
