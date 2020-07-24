#!env python3
# Decodes flip-phone texting codes
# Takes a string of numbers like 84433 and decodes it based on flip-phone keypad texting (84433 => the)

import sys
from collections import OrderedDict

def reverse_ordered_dict(func):
    """
    Decorator that will reverse an OrderedDict returned by func
    """
    def reversed(*args, **kwargs):
        ordered_dict = func(*args, **kwargs)
        d_items = list(ordered_dict.items())
        d_items.reverse()
        return OrderedDict(d_items)
    return reversed


@reverse_ordered_dict   # Reverse it so that we can do find-replace on longer sequences first
def text_to_codes(text, number):
    """
    Takes a string and a keypad number
    Returns an OrderedDict with codes for how many times you press the number mapped to what character you get
    """
    codes = OrderedDict()
    for idx, val in enumerate(text):
        codes[(idx+1)*str(number)] = val
    return codes


def all_codes():
    """
    return all alphabet codes as an ordered dict
    """
    codes = text_to_codes('ABC', 2)
    codes.update(text_to_codes('DEF', 3))
    codes.update(text_to_codes('GHI', 4))
    codes.update(text_to_codes('JKL', 5))
    codes.update(text_to_codes('MNO', 6))
    codes.update(text_to_codes('PQRS', 7))
    codes.update(text_to_codes('TUV', 8))
    codes.update(text_to_codes('WXYZ', 9))
    return codes


def flip_phone_to_text(flip_phone_sequence):
    """
    Converts a flip phone texting code (like 222 28="CAT") to text
    """
    codes = all_codes()
    seq = flip_phone_sequence
    for code, char in codes.items():
        flip_phone_sequence = flip_phone_sequence.replace(code, char)
    flip_phone_sequence = flip_phone_sequence.replace(' ', '').replace('0', ' ')
    return flip_phone_sequence

# Example:
# print(flip_phone_to_text('222 280444660 844330 4428'))  # 'CAT IN THE HAT'

if __name__ == '__main__':
    for line in sys.stdin:
        print(flip_phone_to_text(line))
