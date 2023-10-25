from functools import reduce
import numpy as np  # for storing the count
from collections.abc import Callable
import sys

Plot = Callable
Similar = list[tuple[str, str]]
Matrix = list


def remove_punctuation(token: str) -> str:
    punctuations = [".", ",", "'"]
    return list(reduce(lambda acc, x: acc.replace(x, ""), punctuations, token))


def preprocess(raw_text: str) -> list[str]:
    return [remove_punctuation(x.lower()) for x in raw_text.split()]


def check_word_set(word_set: list[str]) -> list[str]:
    return word_set


def get_word_set(name: str) -> list[str]:
    file_name = name + ".txt" if ".txt" not in name else name
    f = open(file_name)
    text = [x.replace("\n", "") for x in f.readlines()]
    f.close()
    return check_word_set(text)


def PCA(co_occurence: Matrix) -> Plot:
    pass


def cosine_similarity(v1: list[str], v2: list[str]) -> Similar:
    pass


def get_neighbours(text: list[str], i: int, T: list[str], B: list[str], side_length: int) -> list[str]:
    if text[i] not in T:
        return []
    else:
        words = text[i-side_length, i] + text[i+1, i+side_length]
        return list(filter(lambda x: x in B, words))


def co_occurence_matrix(text: list[str], T: list[str], B: list[str], weights, window: int) -> Matrix:
    # On commence à la position 2 (fenêtre de 5)
    # On fini à la position (n-1) - 2 (fenêtre de 5)
    # TODO : Check if window is odd
    # TODO : use the weights parameter
    side_length = window // 2
    [get_neighbours(text, i, T, B, side_length)
        for i in range(side_length, len(text) - (1+side_length))]


def tp1(raw_text: str) -> tuple[Plot, Similar]:
    text = preprocess(raw_text)
    B = get_word_set("B")  # word vector basis
    T = get_word_set("T")  # word for similarity and clustering
    point_wise_mutual_information = None
    com = co_occurence_matrix(text, T, B, weights=point_wise_mutual_information, window=5)
    plot = PCA(com)
    similarities = cosine_similarity(T, T)  # use the PPMI co-occurence matrix
    return (plot, similarities)


if len(sys.args) < 3:
    raise Exception("You should put 3 arguments: the B set, the T set and the text file")

# TODO :  check that B.txt  has exactly one word per line, no space and no empty lines
# TODO : create a structure to federate text, B, and T
