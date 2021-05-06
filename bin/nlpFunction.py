

def nlpFunction(someText, hmLines):
    # --------------------------------------------------------------------
    # imports
    import string
    from nltk.corpus import stopwords
    import pandas as pd
    import re

    # ---------------------------------------------------------------------
    # Split out the sentences
    sentences = re.split('!|\.|\?',someText)

    sentences2 = []
    for sentence in sentences:
        sentences2.append(sentence.rstrip())

    # Remove Whitespace
    sentences3 = []
    for sentence in sentences2:
        sentences3.append(sentence.strip())

    # Remove Empty strings
    sentencesSave = []  # 'sentencesSave' will be saved for final output
    for sentence in sentences3:
        if len(sentence) > 0:
            sentencesSave.append(sentence)

    # 'sentences' will be further modified
    sentences = sentencesSave
    print("log: nlpFunction.py: line 32: length of 'sentencesSave' (Valid Sentences): " + str(len(sentences)))

    # ---------------------------------------------------------------------------------------------
    # Preprocess sentences
    noPunc = string.punctuation

    # Remove punctuation
    sentencesA = []
    for sentence in sentences:
        temp = ""
        for char in sentence:
            if char not in noPunc:
                temp += char
        sentencesA.append(temp)

    # Make lowercase
    sentencesB = []
    for sentence in sentencesA:
        sentencesB.append(sentence.lower())

    # cache sentences
    sentences = sentencesB

    # Remove stopwords
    words = []

    for sentence in sentences:
        temp = sentence.split()
        for word in temp:
            if word not in stopwords.words('english'):
                words.append(word)

    # ---------------------------------------------------------------------------------
    # Make a dataframe of the word vs wordFrequencies,then normalizing to find token weighted frequency
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

    df['wFreq'] = df['Freq'].apply(lambda x: x / denom)  # normalize

    # ---------------------------------------------------------------
    # Scoring sentences via sum of weight frequency of tokens (Then ranking by score)
    swfDict = {}
    wordArray = df['Word']
    wFreq = df['wFreq']

    for i in range(len(wordArray)):
        swfDict[wordArray[i]] = wFreq[i]

    swfList = []

    for sentence in sentences:
        temp = sentence.split()
        score = 0
        for i in temp:
            if i in swfDict:
                score += swfDict[i]
        swfList.append(score)

    # Scoring sentences
    df2 = pd.DataFrame(data=[[sentencesSave[i], swfList[i]] for i in range(len(swfList))], columns=["Sentence", "Score"])
    df2.sort_values(by="Score", ascending=False, inplace=True)  # ranking by score
    df2.reset_index(drop=True, inplace=True)

    # returns a summary of "n" number of sentences
    def numLines(n):
        _out = ""
        for i in df2['Sentence'].head(n):
            _out += i
            _out += "."
            _out += " "

        return _out

    out = numLines(hmLines)

    print("log: nlpFunction.py: line 120: summary: \n    " + out)

    return out

