import re

'''
(1) Email Extraction Function
Create a function that:
receives a text string
finds all valid email addresses
an email is considered valid only if it contains:
an @ symbol
a domain ending in .com, .org, .net or .br
The function must return a list of email strings

(2) ID Validation Function
Create a function that:
receives a list of employee IDs
validates IDs matching the exact pattern: AAA-1234
Where:
AAA = exactly 3 uppercase letters
1234 = exactly 4 digits
The function must return:
a list of valid IDs
a list of invalid IDs

Create a function that:
attempts to read a .txt file from disk
uses try/except to handle errors such as:
file not found
invalid encoding
returns the file content as a string
returns an error message instead of crashing
'''

DOMAINS = [".com",".org",".net",".br"]

def EmailExtraction(s):
    wordList = s.split()
    emails = []
    for i in wordList:
        if re.match(r"[^\w]", i[-1:]):
            i = i[0:-1]
        if re.match(r"\w+(.)?\w+@.*", i):
            if i[-4:] in DOMAINS or i[-3:] in DOMAINS:
                emails.append(i)

    return emails
    
def idExtraction(s):
    wordList = s.split()
    ids = []
    invalidIds = []
    for i in wordList:
        if re.match(r"[^\w]", i[-1:]):
            i = i[0:-1]
        if re.match(r"[A-Z]{3}(-)[0-9]{4}",i):
            ids.append(i)
        else:
            invalidIds.append(i)

    return ids

def fileReader(file):
    try:
        with open(file,'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File does not exist at {file}")
    except UnicodeDecodeError: #I hope this is the right error for invalid encoding
        print("Encoding error")
    return ""

def WordFrequencyCounter(s):
    wordCount = dict()
    for i in s.lower().split():
        if re.match(r"[^\w]", i[-1:]):
            i = i[0:-1]
        if wordCount.get(i) == None:
            wordCount[i] = 1
        else:
            wordCount[i] = int(wordCount[i])+1
            
    return wordCount

if __name__ == "__main__":

    location = "Project1/sample.txt"
    fileContents = fileReader(location)
    
    emails = EmailExtraction(fileContents)
    for i in emails:
        print(i)

    ids = idExtraction(fileContents)
    for i in ids:
        print(i)

    wordCount = WordFrequencyCounter(fileContents)
    print(wordCount)
