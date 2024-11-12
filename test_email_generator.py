import unittest
from tempgenie.email_generator import generate_temp_email

class TestEmailGenerator(unittest.TestCase):
    def test_generate_temp_email(self):
        email = generate_temp_email()
        self.assertIn("@tempgenie.com", email)

if __name__ == '__main__':
    unittest.main()
