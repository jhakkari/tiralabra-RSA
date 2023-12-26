
class MessageLongerThanModulusError(Exception):
    pass

class CipherService:
    """
    Class responsible for RSA encrypt/decrypt operations.
    """

    def encrypt(self, public_exp, modulus, message):
        """
        Encrypts given plaintext message with RSA-public key (public_exp, modulus).
        Throws MessageLongerThanModulusError if message is too long to be ciphered.
        Returns ciphered message in integer form.
        """

        message_bytes = self.string_to_byte_string(message)
        message_int = self.byte_string_to_int(message_bytes)

        if message_int.bit_length() >= modulus.bit_length():
            raise MessageLongerThanModulusError("Message too long to encrypt")

        message_encrypted = pow(message_int, public_exp, modulus)

        return message_encrypted

    def string_to_byte_string(self, string):
        """
        Converts a string to a sequence of bytes. Big-edian byte order, UTF-8 encoding.
        """

        return string.encode("utf-8")

    def byte_string_to_int(self, byte_string):
        """
        Converts a sequence of bytes (Big-edian byte order) to integer.
        """

        return int.from_bytes(byte_string, "big")

    def decrypt(self, private_exp, modulus, ciphered_message):
        """
        Decrypts given ciphered integer to plaintext with RSA-private key (private_exp, modulus).
        Returns string plaintext message.
        """

        message_decrypted = pow(ciphered_message, private_exp, modulus)

        message_bytes = self.int_to_byte_string(message_decrypted)
        message_plain = self.byte_string_to_string(message_bytes)

        return message_plain

    def int_to_byte_string(self, integer):
        """
        Converts integer to a sequency of bytes. Big-edian byte order.
        """

        count = self.integer_byte_count(integer)
        return integer.to_bytes(count, "big")

    def integer_byte_count(self, integer):
        """
        Calculates the required number of bytes to store a given integer.
        Returns required byte count.
        """

        return (integer.bit_length() + 7) // 8

    def byte_string_to_string(self, byte_string):
        """
        Converts a sequence of bytes (Big-edian byte order) to unicode string.
        Returns decoded string.
        """

        return byte_string.decode("utf-8")
