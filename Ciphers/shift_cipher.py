import argparse
import sys
from collections import Counter


def encode(plaintext: str, shift: int) -> str:
    encoded_text = ""
    print(plaintext, shift)
    for letter in plaintext:
        if letter.isupper():
            encoded_text += chr((ord(letter) - 65 + shift) % 26 + 97)
        elif letter.islower():
            encoded_text += chr((ord(letter) - 97 + shift) % 26 + 97)
        else:
            encoded_text += letter
    return encoded_text


def decode(ciphertext: str, shift=None):
    counter = Counter(ciphertext)
    del counter[' ']
    most_common_letter = counter.most_common(1)[0][0]
    if shift is None:
        shift = ord('e') - ord(most_common_letter) if most_common_letter.islower() else ord('E') - ord(
            most_common_letter)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    upper_alphabet = [i.upper() for i in alphabet]
    plaintext = ""
    for letter in ciphertext:
        if letter.isupper():
            plaintext += upper_alphabet[upper_alphabet.index(letter) - shift % 26]
        elif letter.islower():
            plaintext += alphabet[alphabet.index(letter) - shift % 26]
        else:
            plaintext += letter
    return plaintext


def main(text: str, shift: int, do_encode: bool, do_decode: bool):
    if do_encode:
        print(f'The encoded text of "{text}" with a shift of {shift} is: \n\t{encode(text, shift)}')

    if do_decode:
        if shift == -1:
            shift = None
        print(shift)
        print(f'The decoded text of "{text}" is likely to be: \n\t{decode(text, shift)}')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Perform a Ceaser cipher on a given text.')
    parser.add_argument('--text', '-t', required=True, type=str,
                        help='Text to encode / decode.')
    parser.add_argument('--shift', '-s', required=True, type=int,
                        help='Shift to use when encoding.')
    parser.add_argument('--encode', '-e', required=False, action='store_true',
                        help='Perform encoding on the inputted text.')
    parser.add_argument('--decode', '-d', required=False, action='store_true',
                        help='Perform decoding on the inputted text.')
    args = parser.parse_args()
    main(args.text, args.shift, args.encode, args.decode)
