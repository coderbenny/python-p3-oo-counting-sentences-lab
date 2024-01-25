#!/usr/bin/env python3
import re

class MyString:
    
    def __init__(self, value='MyString'):
        self.value = value

    def value(self):
        return self._value
    
    def set_value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value

    value = property(value,set_value)

    def is_sentence(self):
        return '.' in self.value
        
    def is_question(self):
        return '?' in self.value
        
    def is_exclamation(self):
        return '!' in self.value
        
    def count_sentences(self):
        if not self.value:
            return 0
        return len(re.findall(r'[.!?]+',self.value))
        
word = MyString("Mystery word. I have 3 sentences inside.")
print(word.value)
print(word.count_sentences)