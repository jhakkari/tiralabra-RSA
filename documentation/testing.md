# Testing document

## Unit testing

This project contains and passes 52 tests.

Want a closer look? Code coverage is available at [Codecov](https://app.codecov.io/gh/jhakkari/tiralabra-RSA)

## RSA key-pair creation

### KeyService

Each function of the class responsible for key-pair creation is tested separately and at the end as a whole. This is done by replacing return values of fuctions that include random elements (find_prime and choose_public_key) and replacing with known ones. At the end results are compared to what those should be. 

### Miller-Rabin primality test

Primality test is tested with known prime numbers, pseudoprimes and composite numbers. Known prime numbers used in testing are known as Mersenne prime numbers, and algorithm is tested with 14 of these, varying from 4 digits to 1281 digits. List of Mersenne primes can be found [here](https://www.mersenne.org/primes/). The ones used in testing are Mersenne #5 to Mersenne #19. Program identifies all of these as prime numbers.

Pseudoprimes and composites: program is tested with a few of these, and all are recoqniced as composite numbers.

## Encryption/Decryption

Encryption and decryption is tested by giving program a plaintext message, encrypting it, giving the ciphered message to decrypt function and comparing if it returns the original message. which it does.

## Running tests

All of the above tests are done by using unittest. To run tests again, use following command in the project's root folder:

```bash
poetry run invoke test
```

## Pylint

Run pylint check with command:

```bash
poetry run invoke lint
```