# caesar_cypher.py
# earliest and simplest known cypher (encryption program)

MAX_KEY_SIZE = 26


def get_mode():
    while True:
        mode = input('Do you wish to encrypt or decrypt or brute force a message? ').lower()
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')


def get_message():
    message = input('Enter your message: ')
    return message


def get_key():
    key = 0
    while True:
        try:
            key = int(input('Enter the key number (1-%s) ' % MAX_KEY_SIZE))
            if key > 0 and key <= MAX_KEY_SIZE:
                return key
        except ValueError:
            print('You must enter a number')


def get_translated_message(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated


def main():
    key = 0
    # get mode (encrypt, decrypt or brute force
    mode = get_mode()
    # get message to translate
    message = get_message()

    if mode[0] != 'b':
        # if not brute force, get key number
        key = get_key()

    print('Your translated text is: ')

    if mode[0] != 'b':
        # encrypt and decrypt messages
        print(get_translated_message(mode, message, key))
    else:
        # brute force messages
        for key in range(1, MAX_KEY_SIZE + 1):
            print(key, get_translated_message('decrypt', message, key))


if __name__ == '__main__':
    main()
