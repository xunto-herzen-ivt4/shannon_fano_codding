from collections import Counter
import collections
import math
from base_numeral_system import base_ns


def encode(text: str):
    # Generate codes for letters in sentence
    codes = {}
    q = 0
    for letter, frequency in Counter(text).most_common():
        p = frequency/len(text)
        amount = math.ceil(-math.log(p, 2))
        codes[letter] = base_ns.convert(q, 2, amount).fraction
        nulls = amount - len(codes[letter])
        codes[letter] += [0] * nulls
        q += p

    # Code phrase
    result = []
    for letter in text:
        result += codes[letter]
    return codes, result


def decode(codes: dict, encoded_text: list):
    return ""
