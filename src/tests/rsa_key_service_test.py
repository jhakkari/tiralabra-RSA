import unittest
from unittest.mock import Mock, patch
from math import gcd
from services.rsa_key_service import KeyService


class TestKeyService(unittest.TestCase):

    def setUp(self):
        self.KeyService = KeyService()

    def test_get_random_integer_is_in_correct_range(self):
        num1 = self.KeyService.get_random_integer(5, 10)
        num2 = self.KeyService.get_random_integer(5, 10)
        num3 = self.KeyService.get_random_integer(5, 10)
        num4 = self.KeyService.get_random_integer(5, 10)
        num5 = self.KeyService.get_random_integer(5, 10)

        self.assertGreaterEqual(num1, 5)
        self.assertGreaterEqual(num2, 5)
        self.assertGreaterEqual(num3, 5)
        self.assertGreaterEqual(num4, 5)
        self.assertGreaterEqual(num5, 5)

        self.assertLessEqual(num1, 10)
        self.assertLessEqual(num2, 10)
        self.assertLessEqual(num3, 10)
        self.assertLessEqual(num4, 10)
        self.assertLessEqual(num5, 10)

    def test_lcm_calculates_least_common_multiple_with_odd_parameters(self):
        self.assertEqual(self.KeyService.lcm(21, 6), 42)
        
    def test_lcm_calculates_least_common_multiple_with_even_parameters(self):
        self.assertEqual(self.KeyService.lcm(1248, 7646), 4771104)

    def test_lcm_calculates_least_common_multiple_with_even_and_odd_parameters(self):
        self.assertEqual(self.KeyService.lcm(13, 7646), 99398)

    def test_find_prime_returns_correct_bit_length_number(self):
        prime = self.KeyService.find_prime(1048)
        self.assertLessEqual(prime.bit_length(), 1048)

    def test_find_prime_found_prime_is_in_correct_range(self):
        prime = self.KeyService.find_prime(12)
        self.assertGreaterEqual(prime, 2048)
        self.assertLessEqual(prime, 4095)

    def test_choose_public_exponent_returns_integer_in_correct_range(self):
        an = 780
        public_exponent = self.KeyService.choose_public_exponent(an)
        self.assertGreater(public_exponent, 2)
        self.assertLess(public_exponent, an)

    def test_choose_public_exponent_returns_coprime_integer(self):
        an = 780
        public_exponent = self.KeyService.choose_public_exponent(an)
        greatest_common_divisor = gcd(public_exponent, an)
        self.assertEqual(greatest_common_divisor, 1)

    def test_calculate_private_exponent_returns_correct_result(self):
        public_exponent = 17
        an = 780
        private_exponent = self.KeyService.calculate_private_exponent(public_exponent, an)
        self.assertEqual(private_exponent, 413)

    def test_generate_keys_returns_correct_length_modulus(self):
        modulus = self.KeyService.generate_keys()[1]
        
        self.assertGreaterEqual(modulus.bit_length(), 2047)
        self.assertLessEqual(modulus.bit_length(), 2048)

    @patch.object(KeyService, 'find_prime')
    @patch.object(KeyService, 'choose_public_exponent')
    def test_generate_keys_returns_correctly_generated_keys(self, choose_public_exponent, find_prime):
        find_prime.side_effect = [102652170365089553936097857941129409523339493460760324283944167372847720043987258291913134504493412653731348539304119801967356036477238113454709768590894598516038391219624704664701396892964116602057266621073220870223047539739579676028775808043630767712074799029387454026612080934726261547963835392908681215231,
                                    153983688336911124169952692389502916026977844476379566382954027735076753264937548132252269124312959041228774139594994879658700232946839681870857935632904590401123146951397219696123963418243121540688671622156377657574750337330050185858051785226387156358465114915502237280795415845907447435779164410420240538371]
        choose_public_exponent.return_value = 2**16 + 1

        keys = KeyService().generate_keys()

        self.assertEqual(keys[0], 65537)
        self.assertEqual(keys[1], 15806759808605454081543089205117459062823899550154490429966857246080172513862586631434184367599303545865879937639032852240135208356907996338358167454159329982204148445551912916004346301379030526175387542941603836173901727408813833924028969438922837471361534365024986954598001734615152087530806616270497406110534625862621631360363580309979985853416240095145641670024935693335266884253600019344364652102246862906995885210576525179586293995939887310149623399798829581327288938518526619093674172359891582681771750924795372817606053006297397642542651253339346677657599510494698332092710260870342689782513638238289965128701)
        self.assertEqual(keys[2], 1668492653065761481991833353726315795730704370173470465483997208552930671474107783373291432598050903605459270833259097383566646998968798343981172937644130993955961641769367276047650439349983328104369988625683614109340027310812096072747419088218569740137400589443670823420633480319830006120521446053924454216544563822712593208931155520870688280438086583911637298155897154359172823449853886933172930727521348705412530296498741021755486710476388407489660077373833792340430281064497428585728695423812328282528537573714630107909052097791657414178568700362048956338626438149629464504395493559665361358770397219362703600413)
