import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from components.functions import encrypt_text, decrypt_text

def test_encrypt_text():
    assert encrypt_text("ABC", 3) == "DEF"
    assert encrypt_text("Hello, World!", 3) == "Khoor, Zruog!"
    assert encrypt_text("Python!", 5) == "Udymts!"

def test_decrypt_text():
    assert decrypt_text("DEF", 3) == "ABC"
    assert decrypt_text("Khoor, Zruog!", 3) == "Hello, World!"
    assert decrypt_text("Udymts!", 5) == "Python!"
    
def test_non_alphabetic_characters():
    assert encrypt_text("123!?", 3) == "123!?"
    assert decrypt_text("123!?", 3) == "123!?"

if __name__ == "__main__":
    pytest.main()
