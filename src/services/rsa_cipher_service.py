
class CipherService:

    def encrypt(self, public_exp, modulus, message):
        encoded_message = self.encode(message)
        encrypted_message = [pow(c, public_exp, modulus) for c in encoded_message]

        return ''.join(str(encrypted_message))

    def encode(self, message):
        return [ord(c) for c in message]

