from collections import Counter
from base_numeral_system import base_ns
import math


def encode(text: str):
    # Generate codes for letters in sentence
    codes = {}
    q = 0
    for letter, frequency in Counter(text).most_common():
        p = frequency/len(text)
        amount = math.ceil(-math.log(p, 2))
        code = base_ns.convert(q, 2, amount).fraction
        code += [0] * (amount - len(code))
        codes[letter] = code
        q += p

    # Encode phrase
    result = []
    for letter in text:
        result += codes[letter]

    return codes, result


def decode(codes: dict, encoded_text: list):
    result = ""
    i = 0
    while len(encoded_text) >= i:
        for letter in codes:
            if encoded_text[:i] == codes[letter]:
                encoded_text = encoded_text[i:]
                result += letter
                i = 0
        i += 1
    return result
