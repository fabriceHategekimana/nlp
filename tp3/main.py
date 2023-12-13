from crf_tp3 import train_crf, test_crf
from spacy_tp3 import test_spacy
from module import open_file
import os

datasets = [("da_ddt-ud", "danish"),
            ("en_ewt-ud", "english"),
            ("hr_set-ud", "croatian"),
            ("pt_bosque-ud", "portuguese"),
            ("sk_snk-ud", "slovak"),
            ("sr_set-ud", "serbian"),
            ("sv_talbanken-ud", "swedish"),
            ("zh_gsdsimp-ud", "chinese")]

datasets = [("da_ddt-ud", "danish")]

try:
    os.remove("spacy_reports.txt")
    os.remove("crf_reports.txt")
except Exception as e:
    pass

for dataset in datasets:
    name, language = dataset
    training_file = "datasets/"+name+"-train.iob2"
    testing_file = "datasets/"+name+"-test.iob2"

    # for crfs
    tokens_training, labels_training = open_file(training_file)
    model = train_crf(tokens_training, labels_training)

    # for spacy
    tokens_testing, labels_testing = open_file(testing_file)
    report_crf = test_crf(model, tokens_testing, labels_testing)
    report_spacy = test_spacy(tokens_testing, labels_testing, language)
    with open("crf_reports.txt", "a") as report:
        report.write(name+"\n")
        report.write(report_crf)
        report.write("\n")
    with open("spacy_reports.txt", "a") as report:
        report.write(name+"\n")
        report.write(report_spacy)
        report.write("\n")
