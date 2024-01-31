# Testing document

## Unit testing

This project contains and passes 57 tests.

![coverage](https://github.com/jhakkari/tiralabra-RSA/blob/master/documentation/pictures/coverage_report.png)

Want a closer look? Code coverage is available at [Codecov](https://app.codecov.io/gh/jhakkari/tiralabra-RSA)

## RSA key-pair creation

### KeyService

Each function of the class responsible for key-pair creation is tested separately and at the end as a whole. This is done by replacing the return values of functions that include random elements (find_prime and choose_public_exponent) with known ones. In the end, results are compared to what those should be. 

### Miller-Rabin primality test

The primality test is tested with known prime numbers, pseudoprimes, and composite numbers. Prime numbers used in testing are known as Mersenne prime numbers. The algorithm is tested with 15 of these, varying lengths from 13 bits to 4253 bits. A list of Mersenne primes can be found [here](https://www.mersenne.org/primes/). The ones used in testing are Mersenne #5 to Mersenne #19. The program identifies all of these as prime numbers.

Composite numbers used in testing are created by multiplying two prime numbers together. The bit length of these numbers varies from 1128 bits to 3324 bits. A few "pseudoprimes" are also used during testing. The program recognizes all of these as composite numbers.

## Encryption/Decryption

Each function required for operations is tested separately and at the end as a whole.

To encrypt a message, it needs to be turned into an integer that is smaller than the public key's modulus. To ensure encryption succeeds, the app rejects messages that violate this condition. Rejection is tested with too long message and listening if an exception is raised. 

Encryption and decryption are tested by giving the program a plaintext message, encrypting it, giving the ciphered message to the decrypt function, and comparing if it returns the original message. Which it does.

## Running tests

All of the above tests are done by using unittest. To run tests again, use the following command in the project's root folder:

```bash
poetry run invoke test
```

## Pylint

Run pylint check with command:

```bash
poetry run invoke lint
```
