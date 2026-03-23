from twoFunctions import FileReader,IdExtraction,EmailExtraction,WordFrequencyCounter

if __name__ == "__main__":

    location = "Project1/sample.txt"
    fileContents = FileReader(location)
    
    emails = EmailExtraction(fileContents)
    for i in emails:
        print(i)

    ids = IdExtraction(fileContents)
    for i in ids:
        print(i)

    wordCount = WordFrequencyCounter(fileContents)
    print(wordCount)