# get Baseline.txt
# use transformer library
    # Traine NER classifier by load and fine tune pretrained model:
        # BERT-based  models (encoders)

# output:
#   baseline_results, transfer_learning_result, overall_difference

# todo:
# $ python3 app.py [language]

"""
Bert {
    Model,
    User_definable_layer
}
"""


def write_results(params):
    with open("compare_eval.txt", "w") as file:
        file.write("Hello world")
