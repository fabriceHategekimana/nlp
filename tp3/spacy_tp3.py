import spacy
from functools import reduce
from collections import defaultdict
from sklearn.metrics import classification_report


def get_token_bio(doc):
    entities = doc.ents
    new_entities = reduce(lambda x, y: x + y,
                          [e.text.split(" ") for e in entities])
    annotations_bio = ["O"] * len(doc)

    for entite in entities:
        for i in range(entite.start, entite.end):
            if i == entite.start:
                annotations_bio[i] = "B-" + entite.label_
            else:
                annotations_bio[i] = "I-" + entite.label_
    return new_entities, annotations_bio


def test_spacy(tokens, labels, language="french"):
    lan = defaultdict(lambda: "xx_ent_wiki_sm")
    lan["danish"] = "da_core_news_sm"
    lan["chinese"] = "zh_core_web_sm"
    lan["portuguese"] = "pt_core_news_sm"
    lan["english"] = "en_core_web_sm"
    lan["french"] = "fr_core_news_sm"

    nlp = spacy.load(lan[language])
    text = " ".join(tokens)
    tokens2, labels2 = get_token_bio(nlp(text))
    dic = {tok: lab for tok, lab in zip(tokens, labels)}
    labels2 = [dic[t] for t in tokens]
    return classification_report(labels, labels2)
