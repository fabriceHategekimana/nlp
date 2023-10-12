import numpy as np  # for storing the count
from collections.abc import Callable

Plot = Callable
Similar = list[tuple[str, str]]
Matrix = list


def preprocess(raw_text: str) -> list[str]:
    # separate by white space (splitting)
    # lowercase
    # remove all the punctuation
    pass


def get_word_set(name: str) -> list[str]:
    pass


def PCA(co_occurence: Matrix) -> Plot:
    pass


def cosine_similarity(v1: list[str], v2: list[str]) -> Similar:
    pass


def co_occurence_matrix(T, B, weights, window) -> Matrix:
    pass


def tp1(raw_text: str) -> tuple[Plot, Similar]:
    text = preprocess(raw_text)
    B = get_word_set("B")  # word vector basis
    T = get_word_set("T")  # word for similarity and clustering
    point_wise_mutual_information = None
    com = co_occurence_matrix(T, B, weights=point_wise_mutual_information, window=5)
    plot = PCA(com)
    similarities = cosine_similarity(T, T)  # use the PPMI co-occurence matrix
    return (plot, similarities)
