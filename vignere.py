"""
Crack the Vignere cipher key
"""

import string
import argparse

# Create a Vignere cipher table
TABLE = [list(l) for l in """ABCDEFGHIJKLMNOPQRSTUVWXYZ
BCDEFGHIJKLMNOPQRSTUVWXYZA
CDEFGHIJKLMNOPQRSTUVWXYZAB
DEFGHIJKLMNOPQRSTUVWXYZABC
EFGHIJKLMNOPQRSTUVWXYZABCD
FGHIJKLMNOPQRSTUVWXYZABCDE
GHIJKLMNOPQRSTUVWXYZABCDEF
HIJKLMNOPQRSTUVWXYZABCDEFG
IJKLMNOPQRSTUVWXYZABCDEFGH
JKLMNOPQRSTUVWXYZABCDEFGHI
KLMNOPQRSTUVWXYZABCDEFGHIJ
LMNOPQRSTUVWXYZABCDEFGHIJK
MNOPQRSTUVWXYZABCDEFGHIJKL
NOPQRSTUVWXYZABCDEFGHIJKLM
OPQRSTUVWXYZABCDEFGHIJKLMN
PQRSTUVWXYZABCDEFGHIJKLMNO
QRSTUVWXYZABCDEFGHIJKLMNOP
RSTUVWXYZABCDEFGHIJKLMNOPQ
STUVWXYZABCDEFGHIJKLMNOPQR
TUVWXYZABCDEFGHIJKLMNOPQRS
UVWXYZABCDEFGHIJKLMNOPQRST
VWXYZABCDEFGHIJKLMNOPQRSTU
WXYZABCDEFGHIJKLMNOPQRSTUV
XYZABCDEFGHIJKLMNOPQRSTUVW
YZABCDEFGHIJKLMNOPQRSTUVWX
ZABCDEFGHIJKLMNOPQRSTUVWXY""".split()]


def crack_vignere_key(plaintext, ciphertext):
    """
    Crack a Vignere cipher key given some plaintext and ciphertext
    The pt and ct might be at least as long as the key
    """
    # For each character in the plaintext, figure out which letter in the key
    # would lead to the ciphertext
    key = ''
    for pt, ct in zip(list(plaintext), list(ciphertext)):
        pt_idx = string.ascii_uppercase.find(pt)
        ct_idx = TABLE[pt_idx].index(ct)
        key_char = string.ascii_uppercase[ct_idx]
        key += key_char
    return key

def main():
    parser = argparse.ArgumentParser("Crack a Vignere cipher key given some plaintext and ciphertext. Note the key repeats and may be shifted; look for a recognizable key in the output from this program.")
    parser.add_argument('--plaintext', '-p', required=True)
    parser.add_argument('--ciphertext', '-c', required=True)
    args = parser.parse_args()
    print('Key is: %s' % crack_vignere_key(args.plaintext.upper(), args.ciphertext.upper()))

if __name__ == '__main__':
    main()