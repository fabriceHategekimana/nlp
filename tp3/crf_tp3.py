import pycrfsuite
from sklearn.metrics import classification_report


def train_crf(tokens, labels):
    X_train = tokens
    Y_train = labels

    model = pycrfsuite.Trainer()

    for xseq, yseq in zip(X_train, Y_train):
        model.append([xseq], [yseq])

    model.set_params({
        "c1": 1.0,
        "c2": 1e-3,
        "max_iterations": 100,
        "feature.possible_transitions": True
    })

    model.train("chemin_vers_votre_modele.crfsuite")
    model = pycrfsuite.Tagger()
    model.open("chemin_vers_votre_modele.crfsuite")
    return model


def test_crf(model, tokens, labels):
    labels_pred = [model.tag([x]) for x in tokens]
    return classification_report([[x] for x in labels], labels_pred)
