# Caesar Cipher Project

A simple implementation of the Caesar Cipher in Python, a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- Encrypt and decrypt text using a specified shift.
- Supports uppercase and lowercase letters.
- Non-alphabetic characters remain unchanged.

## Requirements

- Python 3.x

## Installation

Clone the repository:

```sh
git clone https://github.com/yourusername/caesar-cipher.git
cd caesar-cipher
```

## Usage

### Encrypt

```sh
python caesar_cipher.py --mode encrypt --shift 3 --text "Hello, World!"
```

### Decrypt

```sh
python caesar_cipher.py --mode decrypt --shift 3 --text "Khoor, Zruog!"
```

## Examples

### Encrypt

```sh
python caesar_cipher.py --mode encrypt --shift 4 --text "OpenAI"
```

Output: `SrgiEM`

### Decrypt

```sh
python caesar_cipher.py --mode decrypt --shift 4 --text "SrgiEM"
```

Output: `OpenAI`
