#!\Users\kolok\anaconda3\envs\py38\python3.8
"""
ROFL

"""
import string
from nltk.corpus import stopwords
import pandas as pd
import re

def nlpFunction(someText, hmLines):
    # ---------------------------------------------------------------------
    # Split out the sentences
    sentences = re.split("\!|\.|\?",someText)
    sentences2 = []
    for sentence in sentences:
        sentences2.append(sentence.rstrip())

    # Remove Whitespace
    sentences3 = []
    for sentence in sentences2:
        sentences3.append(sentence.strip())

    print("    .")
    # Remove Empty strings
    sentences4 = []
    for sentence in sentences3:
        if len(sentence) > 0:
            sentences4.append(sentence)

    sentences = sentences4
    # ---------------------------------------------------------------------------------------------
    # Preprocess sentences
    import string
    nopunc = string.punctuation
    print("    .")
    # Remove punctuation
    sentencesA = []
    for sentence in sentences:
        temp = ""
        for char in sentence:
            if char not in nopunc:
                if char != "-":  # toggle
                    temp += char
        sentencesA.append(temp)

    # Lowercase
    sentencesB = []
    for sentence in sentencesA:
        sentencesB.append(sentence.lower())

    sentences = sentencesB

    words = []
    print("    .")
    from nltk.corpus import stopwords

    for sentence in sentences:
        temp = sentence.split()
        for word in temp:
            if word not in stopwords.words('english'):
                words.append(word)

    # ---------------------------------------------------------------------------------
    # Make a dataframe of the word/wordFrequencies (and normalizing frequencies)

    import pandas as pd
    print("    .")
    freqDict = {}
    for word in words:
        if word not in freqDict:
            freqDict[word] = 1
        else:
            freqDict[word] += 1

    setWords = set(words)
    setWordsList = list(setWords)

    df = pd.DataFrame(data=[[i, freqDict[i]] for i in setWordsList], columns=["Word", "Freq"])

    df.sort_values(by="Freq", ascending=False, inplace=True)

    denom = df["Freq"].iloc[0]
    print(denom)

    df['wFreq'] = df['Freq'].apply(lambda x: x / denom) # normazine freuencies
    print("    .")

    # ---------------------------------------------------------------
    # Scoring sentences
    # sentences: sum of weighted frequencies
    swf = []

    swfDict = {}
    wordArray = df['Word']
    wFreq = df['wFreq']

    for i in range(len(wordArray)):
        swfDict[wordArray[i]] = wFreq[i]

    swfList = []
    print("    .")
    for sentence in sentences:
        temp = sentence.split()
        score = 0
        for i in temp:
            if i in swfDict:
                score += swfDict[i]
        swfList.append(score)

    df2 = pd.DataFrame(data=[[sentences4[i], swfList[i]] for i in range(len(swfList))], columns=["Sentence", "Score"])

    df2.sort_values(by="Score", ascending=False, inplace=True)

    df2.reset_index(drop=True, inplace=True)
    print("    .")


    def numLines(num):
        temp = ""
        for i in df2['Sentence'].head(num):
            temp += i
            temp += "."
            temp += " "

        #print(temp)
        return temp

    #hmLines = int(input("How many lines should we summarize to?: "))
    #hmLines = 3
    print("")
    out = numLines(hmLines)

    return out

