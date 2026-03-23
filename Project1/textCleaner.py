import re

'''
Create a class named TextCleaner with:
Attributes:
original_text
Methods:
remove_extra_spaces()
remove_special_characters() (keep only letters, numbers, spaces, dots, commas)
to_lowercase()
The class must return the cleaned text.
'''

class TextCleaner():
    def __init__(self, original_text):
        self.original_text = original_text
    
    def remove_extra_spaces(original_text):
        return re.sub(r"(  )", "", original_text.strip())
    
    def remove_special_characters(original_text):
        return re.sub(r"(^[a-z][A-Z][0-9]( )(,)(.)(@)(-))", "", original_text)
    
    def to_lowercase(original_text):
        return original_text.lower()
