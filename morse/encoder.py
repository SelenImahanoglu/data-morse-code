"""
This module provides functions to encode text into Morse code.
"""

from morse.mapping import MORSE

def encode_word(word):
    """
    Encodes a single word into Morse code.
    Letters are separated by a space.
    """
    # Alfanümerik olmayan karakterleri (virgül, nokta vb.) filtreleyerek encode ediyoruz
    encoded_chars = [MORSE[char.upper()] for char in word if char.upper() in MORSE]
    return " ".join(encoded_chars)


def encode(text):
    """
    Encodes the given text into Morse code.
    Words are separated by a pipe (|) and letters by a space.
    """
    words = text.split()
    encoded_words = [encode_word(word) for word in words]
    # Testlerin beklediği formatta, pipe '|' işaretinin yanına boşluk koymuyoruz
    return "|".join(encoded_words)
