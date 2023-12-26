import unittest
from services.rsa_cipher_service import CipherService, MessageLongerThanModulusError


class TestCipherService(unittest.TestCase):
    def setUp(self):
        self.cipher_service = CipherService()

    def test_string_to_byte_string_is_in_big_edian_order(self):
        result = self.cipher_service.string_to_byte_string("abc")
        self.assertEqual(result, b"\x61\x62\x63")

    def test_string_to_byte_string_converts_letters(self):
        string = "abcdefghijklmnopqrstuvwxyz"
        b_string = b"abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.cipher_service.string_to_byte_string(string), b_string)

    def test_byte_string_to_int_converts_bytes_correctly(self):
        self.assertEqual(self.cipher_service.byte_string_to_int(b"\x61"), 97)
        self.assertEqual(self.cipher_service.byte_string_to_int(b"\x3A"), 58)
        self.assertEqual(self.cipher_service.byte_string_to_int(b"\x61\x62\x63"), 6382179)

    def test_byte_string_to_string_encodes_string_correctly(self):
        byte_string = b"\x48\x65\x6C\x6C\x6F\x20\x77\x6F\x72\x6C\x64"
        self.assertEqual(self.cipher_service.byte_string_to_string(byte_string), "Hello world")

    def test_int_to_byte_string_concerts_correctly(self):
        self.assertEqual(self.cipher_service.int_to_byte_string(97), b"\x61")
        self.assertEqual(self.cipher_service.int_to_byte_string(58), b"\x3A")
        self.assertEqual(self.cipher_service.int_to_byte_string(6382179), b"\x61\x62\x63")

    def test_integer_byte_count_returns_correct_count(self):
        self.assertEqual(self.cipher_service.integer_byte_count(0), 0)
        self.assertEqual(self.cipher_service.integer_byte_count(97), 1)
        self.assertEqual(self.cipher_service.integer_byte_count(255), 1)
        self.assertEqual(self.cipher_service.integer_byte_count(256), 2)
        self.assertEqual(self.cipher_service.integer_byte_count(1342), 2)

    def test_encrypt_rejects_too_long_message(self):
        public_exponent = 17
        modulus = 3233
        message = "abc"
        error = False

        try:
            self.cipher_service.encrypt(public_exponent, modulus, message)
        except MessageLongerThanModulusError:
            error = True

        self.assertTrue(error)

    def test_decrypt_returns_original_message_from_ciphertext(self):
        public_exponent = 1576441832122077688667251877600224711137706778361721416082124688615992129092196471229349070544992269643379325272380042266767067836776240863789382136483580857562787102956354119049985470078575549688625229561887812681116249613978082251768082027339547096243143460354871136947680801619902027280073447324985652979907001284529751194321485224287893402986291850816096924205607221010429470712041622818233086572059849701729044909204018338351607552793112414746474575001139524923151846295351401717446645150777835718841835358511657963835761984328613221214615268053436012739716261250408945790584874433671888451996492306642422087113
        private_exponent = 3333164768098867517127545404502319326429015686576030142569693095189610339576553426389960856991886092759288857098056442516003293851028448786927842941371357937186329595901268643100269394149810457268128762524431067745083419826977452436457469856365372827759119256351274073134492829403117235493105673427825382292987713695082018539496003151912398242126995900008424694600439552088776064340899322096127233683317298269019698151772142372762519362161626542451702925186223512023113137128202880273692776084160673665871673985125652061970769930693624428057215452915457893697449022514675220973353930432276578765121165688593780144147
        modulus = 21769939669635700060318952654863389102570244673372938168940300903466756706527845227741391036896496644255918400223288612595187700899630832915693018030154265208108198305467073500156133092651184650405038550780889559428197807800476915224523058723713050133158408114314184211838866944485106947862590596358409812026127534656097757586993967991967947875223627366286386530005020835230439234861802799619411848015995510624351312012740262358758640600135556318894452341758713294285301193520683707270218854050422858962951136008029948306167545005579519369815748006140916608912107138998895557887862965461559740820782394861574716545517
        message = "abcdefqhijklmnopqrstuvwxyzåäö1234567890"

        encrypted_message = self.cipher_service.encrypt(public_exponent, modulus, message)
        decrypted_message = self.cipher_service.decrypt(private_exponent, modulus, encrypted_message)

        self.assertEqual(decrypted_message, message)