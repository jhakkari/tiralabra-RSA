
class CipherService:

    def encrypt(self, public_exp, modulus, message):
        encoded_message = self.encode(message)
        encrypted_message = [pow(c, public_exp, modulus) for c in encoded_message]

        return encrypted_message

    def encode(self, message):
        return [ord(c) for c in message]

    def decrypt(self, private_exp, modulus, ciphered_message):
        message = [pow(c, private_exp, modulus) for c in ciphered_message]
        decoded_message = self.decode(message)

        return decoded_message

    def decode(self, message):
        return "".join(chr(c) for c in message)

