import string

def start():
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E']

    def encrypt():
        
        word = input('Type your secret word:\n').lower()
        shift = int(input('Type the shift number (Max = 5):\n'))

        new_word = []

        for letter in word:
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                new_word.append(alphabet[letter_index + shift])
            else:
                new_word.append(" ")

        encrypted_word = ''.join(new_word)
        print(encrypted_word)

    def decrypt():
        to_decrypt = input("Type the word to decrypt:\n")
        shift = int(input('Type the shift number (Max = 5):\n'))

        decrypted_list = []
        
        for letter in to_decrypt:
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                decrypted_list.append(alphabet[letter_index - shift])
            else:
                decrypted_list.append(" ")
        
        decrypted_word = ''.join(decrypted_list)
        print(decrypted_word)

    action = input('Do you want to encrypt or decrypt:\n').lower()

    if action == 'encrypt':
        encrypt()
    else:
        decrypt()

start()