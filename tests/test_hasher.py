import unittest
from hash_maker import hash_password, verify_password

class TestHasher(unittest.TestCase):

    def test_hash_and_verify_password(self):
        password = 'my_secure_password'
        hashed_pw = hash_password(password)
        self.assertTrue(verify_password(hashed_pw, password))

    def test_incorrect_password(self):
        password = 'my_secure_password'
        hashed_pw = hash_password(password)
        self.assertFalse(verify_password(hashed_pw, 'wrong_password'))

if __name__ == '__main__':
    unittest.main()