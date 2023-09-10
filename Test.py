import random

def readFile(fileName):
    with open(fileName, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def separateData(lines):
    result = {}
    for line in lines:
        # Split each line by ':' to separate key and value
        parts = line.split(':')
        if len(parts) == 2:
            key = parts[0].strip() # Remove leading/trailing spaces
            value = parts[1].strip() # Remove leading/trailing spaces
            result[key] = value
    return result

def reverseSeparateData(lines):
    result = {}
    for line in lines:
        # Split each line by ':' to separate key and value
        parts = line.split(':')
        if len(parts) == 2:
            key = parts[1].strip() # Remove leading/trailing spaces
            value = parts[0].strip() # Remove leading/trailing spaces
            result[key] = value
    return result

frenchVocabulary = separateData(readFile('Vocabulary.txt'))
englishVocabulary = reverseSeparateData(readFile('Vocabulary.txt'))

def testUser(vocab, dictionary):
    print(vocab)
    userInput = input('Your answer: ')
    if engOrFr == 'F':
        if userInput == frenchVocabulary[vocab]:
            print('Bingo!')
        else:
            testUser(vocab, engOrFr)
    elif engOrFr == 'E':
        if userInput == englishVocabulary[vocab]:
            print('Bingo!')
        else:
            testUser(vocab, engOrFr)

while True:
    engOrFr = random.choice(['F', 'E'])
    if engOrFr == 'F':
        word = random.choice(list(frenchVocabulary.keys()))
    elif engOrFr == 'E':
        word = random.choice(list(englishVocabulary.keys()))
    
    testUser(word, engOrFr)
    
    userInput = input('Continue? (Y/N/R)')
    if userInput == 'N':
        break