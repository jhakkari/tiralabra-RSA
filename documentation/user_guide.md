# User guide

## Installation

1. Download project to your computer and unzip it

2. Navigate to project's root folder and install dependencies with command:

```bash
poetry install
```

3. Start the app with command:

```bash
poetry run invoke start
```

## Using the app

This app consists of three views: Keys, Encrypt and Decrypt. You can change between these views by clicking tabs name in view's top left corner.

### Keys tab

Here you can create 2048 bit RSA key-pairs by clicking "Generate" -button at the bottom of the view.

Public key: consists of two parts. Public exponent and modulus. Separated by comma and a plankspace.

Private key: consists of two parts. Private exponent and modulus. Separated by comma and a plankspace.

### Encrypt tab

In this tab you can encrypt messages with public key created earlier.

Required input: 
- Public key: consists of two parts, public exponent and modulus, separated by a comma and a plankspace. You can copy and paste this straight from the previous tab.
- Message: whatever text you would like to cipher.

Cipher the given message by clicking "Encrypt" -button at the bottom of the view. Encrypted message is printed to GUI.

### Decrypt tab

Here you can decrypt ciphered messages with private key created earlier.

Required input:
- Private key: consists of two parts, private exponent and modulus, separated by a comma and a plankspace. You can copy and paste this straight from the keys tab.
- Encrypted message: ciphered message you would like decrypt.

Click "Decrypt" -button at the bottom of the view. Original plaintext message is printed to the GUI.