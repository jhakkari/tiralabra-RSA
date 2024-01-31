# User guide

## Installation

1. Download the project to your computer and unzip it

2. Navigate to the project's root folder and install dependencies with the command:

```bash
poetry install
```

3. Start the app with command:

```bash
poetry run invoke start
```

## Using the app

This app consists of three views: Keys, Encrypt and Decrypt. You can change between these views by clicking the tab name in the view's top left corner.

### Keys tab

Here you can create 2048-bit RSA key-pairs by clicking the "Generate" -button at the bottom of the view.

![keys](https://github.com/jhakkari/tiralabra-RSA/blob/master/documentation/pictures/keys_view.png)

Public key: consists of two parts. Public exponent and modulus. Separated by a comma and a blank space.

Private key: consists of two parts. Private exponent and modulus. Separated by a comma and a blank space.

### Encrypt tab

In this tab, you can encrypt messages with a public key created earlier.

![encrypt](https://github.com/jhakkari/tiralabra-RSA/blob/master/documentation/pictures/encrypt_view.png)

Required input: 
- Public key: consists of two parts, public exponent and modulus, separated by a comma and a blank space. You can copy and paste this straight from the previous tab.
- Message: whatever text you would like to cipher.

Cipher the given message by clicking the "Encrypt" -button at the bottom of the view. Encrypted message is printed to GUI.

If the given message is too long to be encrypted, the following warning is shown.

![warning](https://github.com/jhakkari/tiralabra-RSA/blob/master/documentation/pictures/encrypt_view_error.png)

### Decrypt tab

Here you can decrypt ciphered messages with a private key created earlier.

![decrypt](https://github.com/jhakkari/tiralabra-RSA/blob/master/documentation/pictures/decrypt_view.png)

Required input:
- Private key: consists of two parts, private exponent and modulus, separated by a comma and a blank space. You can copy and paste this straight from the keys tab.
- Encrypted message: ciphered message you would like to decrypt.

Click the "Decrypt" -button at the bottom of the view. The original plaintext message is printed to the GUI.
