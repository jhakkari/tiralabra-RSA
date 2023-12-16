import unittest
from services.rsa_cipher_service import CipherService


class TestCipherService(unittest.TestCase):
    def setUp(self):
        self.cipher_service = CipherService()

    def test_encode_returns_correct_unicode_list(self):
        message = "Hello world!"
        encoded_message = self.cipher_service.encode(message)

        self.assertEqual(encoded_message, [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33])

    def test_decode_returns_correct_string_given_unicode_list(self):
        encoded_message = [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]
        message = self.cipher_service.decode(encoded_message)

        self.assertEqual(message, "Hello world!")
        
    def test_encrypt_returns_correctly_ciphered_list(self):
        encrypted_message = self.cipher_service.encrypt(17, 3233, "Hello world!")
        self.assertEqual(encrypted_message, [3000, 1313, 745, 745, 2185, 1992, 1107, 2185, 2412, 745, 1773, 1853])

    def test_decrypt_returns_correctly_decrypted_message(self):
        decrypted_message = self.cipher_service.decrypt(413, 3233, [3000, 1313, 745, 745, 2185, 1992, 1107, 2185, 2412, 745, 1773, 1853])
        self.assertEqual(decrypted_message, "Hello world!")