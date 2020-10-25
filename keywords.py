import spacy
def keywords(sentence):

    nlp = spacy.load("en")
    doc = nlp(sentence.lower())
    keywords = []
    for token in doc:
        if token.pos_ == 'NOUN' or token.pos_ == 'VERB' or token.pos_ == 'ADJ' or token.pos_ == "PROPN":
            keywords.append(token.text)
            
    return keywords

