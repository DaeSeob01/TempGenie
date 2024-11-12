import unittest
from tempgenie.password_generator import suggest_password

class TestPasswordGenerator(unittest.TestCase):
    def test_suggest_password(self):
        password = suggest_password(12)
        self.assertEqual(len(password), 12)

if __name__ == '__main__':
    unittest.main()
