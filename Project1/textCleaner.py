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
    
    def remove_extra_spaces(original_text): #removes 2+ spaces
        withoutTwoSpace = ""
        for i in range(0,len(original_text)-1):
            if not (original_text[i] == ' ' and original_text[i+1] == ' '):
                withoutTwoSpace += original_text[i]
        withoutTwoSpace+=original_text[-1:]

        return withoutTwoSpace
    
    def remove_special_characters(original_text): #removes all special except ( )(,)(.)(@)(-)
        return re.sub(r"(^[a-z][A-Z][0-9]( )(,)(.)(@)(-))", "", original_text)
    
    def to_lowercase(original_text): #to lower
        return original_text.lower()
