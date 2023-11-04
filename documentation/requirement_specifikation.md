# Requirement specifikation

The aim of this project is to generate secure cryptographic keys in compliance with the RSA (Rivest-Shamir-Adleman) cryptosystem. This app can also encrypt/decrypt text using generated keys. 

## Algorithms

### Miller-Rabin Primality Test

Required large prime numbers are chosen using Miller-Rabin primality test.

### Extended Euclidean Algorithm

Used to calculate greatest common divisor and during key creation.

### RSA (Rivest-Shamir-Adleman) Algorithm

At the end, cryptographic keys are generated based on output of the above algorithms using RSA-algorithm. Key length is 1024 bits or more.

## Inputs and outputs

- Key generation: No input needed.
- Encryption: Recipient's public key and message to be ciphered needed. Ciphered message printed to GUI.
- Decryption: Recipient's private key and ciphered message required. Original message printed to GUI.

## Other information

- Programming language: Python
- Code/documentation language: English
- Degree program: Bachelor’s in Computer Science

(I have taken basic programming courses using java, so peer review with that is also a possibility)

## Sources

- [RSA (cryptosystems)](https://en.wikipedia.org/wiki/RSA_(cryptosystem)), Wikipedia 2023
- [Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test), Wikipedia 2023
- [Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm), Wikipedia 2023
