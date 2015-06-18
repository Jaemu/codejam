import re
VOWELS = "AEIOUYaeiouy"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZbcdfghjkmnpqrstvwxz"

def filterForStriped(x):
    startsWithVowel = len(re.findall('^[' + VOWELS + ']', x)) > 0
    isStriped = False
    if(len(re.findall('[0-9]+', x)) is 0 and len(x) > 1):
        for i in xrange(len(x)):
            if(i%2 > 0):
                isStriped = startsWithVowel is not(len(re.findall('["' + VOWELS + '"]', x[i])) > 0)
            else:
                isStriped = startsWithVowel is (len(re.findall('["' + VOWELS + '"]', x[i])) > 0)
            if(not isStriped):
                return isStriped
    return isStriped


def checkio(text):
    numWords = 0
    textList = re.split('\W+', text)
    stripedWords = [x for x in textList if filterForStriped(x)]
    print(stripedWords)
    return len(stripedWords)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
