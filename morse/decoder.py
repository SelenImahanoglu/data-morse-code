"""
This module provides functions to decode Morse code back into text.
"""
from morse.mapping import MORSE

# Morse -> Harf eşleşmesi için sözlüğü ters çeviriyoruz
DECODE_MAP = {value: key for key, value in MORSE.items()}

def decode_word(word):
    """
    Decodes a single Morse code word into text.
    Letters are expected to be separated by a space.
    """
    chars = word.split()
    decoded_chars = [DECODE_MAP[char] for char in chars if char in DECODE_MAP]
    return "".join(decoded_chars)

def decode(morse_code):
    """
    Decodes the given Morse code into text.
    Words are expected to be separated by a pipe (|).
    """
    words = morse_code.split("|")
    decoded_words = [decode_word(word) for word in words]
    return " ".join(decoded_words)


if __name__ == "__main__":
    # Example usage for one word
    EXAMPLE_MORSE_WORD = ".... . -.--"
    DECODED_WORD = decode_word(EXAMPLE_MORSE_WORD)
    print(f"Decoded Morse word '{EXAMPLE_MORSE_WORD}' to text: '{DECODED_WORD}'")

    # Example usage for one sentence
    EXAMPLE_MORSE_SENTENCE = ".... . -.--|.--- ..- -.. ."
    DECODED_TEXT = decode(EXAMPLE_MORSE_SENTENCE)
    print(f"Decoded Morse sentence '{EXAMPLE_MORSE_SENTENCE}' to text: '{DECODED_TEXT}'")
