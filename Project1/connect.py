from twoFunctions import FileReader,IdExtraction,EmailExtraction,WordFrequencyCounter
from textCleaner import TextCleaner

if __name__ == "__main__":

    location = "Project1/sample.txt"
    fileContents = FileReader(location)

    fileContents = TextCleaner.remove_extra_spaces(fileContents)
    fileContents = TextCleaner.remove_special_characters(fileContents)
    fileContents = TextCleaner.to_lowercase(fileContents)
    print(f"File Contents after formatting: \n{fileContents}")

    emails = EmailExtraction(fileContents)
    print("Emails Extracted:")
    for i in emails:
        print(i)
    print()

    ids = IdExtraction(fileContents.upper()) #had to make it upper since the function needs to have AAA not aaa.
    print("IDs:")
    for i in ids:
        print(i)
    print()

    wordCount = WordFrequencyCounter(fileContents)
    print("Word Count Dictionary:")
    print(wordCount)