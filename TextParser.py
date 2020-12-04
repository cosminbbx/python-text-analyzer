import re

words = 0
sentences = 0
CNPs = set()
phones = set()
letters = {}
letterCount = 0

separators = "?!. ,;:\n"
sentencesSeparators = "?.!"


def parse(text):
    global words
    global sentences
    global CNPs
    global phones
    global letterCount

    currentWord = ""
    currentSentence = ""

    if len(text)==0: 
        return formatInformation()
    for i in range(0,len(text)):
        character = text[i]

        currentWord = verifyWord(currentWord,character)
        currentSentence = verifySentence(currentSentence,character)
            
        addLetter(character)

    currentWord = verifyWord(currentWord,".")
    currentSentence = verifySentence(currentSentence,".")

    return formatInformation()

def verifyWord(currentWord,character):
    global words
    global CNPs
    global phones

    if isSeparator(character):
        if isPhoneNumber(currentWord):
            phones.add(currentWord)
        if isCNP(currentWord):
            CNPs.add(currentWord)

        if len(currentWord) > 0:
            words = words + 1
        return ""
    else:
        return currentWord + character

def verifySentence(currentSentence,character):
    global sentences

    if isSentenceSeparator(character):
        if len(currentSentence) > 0:
            sentences = sentences + 1
        return ""
    else:
        return currentSentence + character


def formatInformation():
    return [words,sentences,list(CNPs),list(phones),letters,letterCount]

def addLetter(character):
    global letterCount
    if character not in separators:
        letterCount = letterCount + 1
        if character in letters:
            letters[character] = letters[character] + 1
        else:
            letters[character] = 1

def isSeparator(character):
    if character in separators:
        return True
    else:
        return False

def isSentenceSeparator(character):
    if character in sentencesSeparators:
        return True
    else:
        return False

def hasOnlyNumbers(text):
    if re.match(r'^[0-9]*$', text):
        return True
    else:
        return False

def isPhoneNumber(text):
    if len(text) == 10 and text[0] == "0" and text[1] == "7":
        return hasOnlyNumbers(text)
    else:
        return False

def isCNP(text):
    if len(text) == 13:
        return hasOnlyNumbers(text)
    else:
        return False
