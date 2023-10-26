from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import KernelPCA
from collections.abc import Callable
from collections import namedtuple
from functools import reduce
import pandas as pd
import numpy as np
import sys

Plot = Callable
Similar = list[tuple[str, str]]
Matrix = pd.DataFrame
Data = namedtuple("Data", "text B T")


def remove_punctuation(token: str) -> str:
    punctuations = [".", ",", "'", "-"]
    return reduce(lambda acc, x: acc.replace(x, ""), punctuations, token)


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


def get_neighbours(configuration: Data, i: int, side_length: int) -> list[tuple[str, str]]:
    if configuration.text[i] not in configuration.T:
        return []
    else:
        words = configuration.text[i-side_length:i] + configuration.text[i+1:i+side_length]
        # I don't return a real tuple because np.unique encode it strangelly later
        return [f"{configuration.text[i]},{word}" for word in filter(lambda x: x in configuration.B, words)]


def PMI(configuration: Data, df: pd.DataFrame) -> pd.DataFrame:
    # val = log2(counts/(configuraiton.text.probe_count(A)*configuration.text.prob_count(B)))
    # TODO : implement the method to gain a weight that's more representative
    return df


def create_counter(list_of_couples: list[str]) -> pd.DataFrame:
    unique, counts = np.unique(list_of_couples, return_counts=True)
    terms = [couple.split(",")[0] for couple in unique]
    related = [couple.split(",")[1] for couple in unique]
    return pd.DataFrame({'terms': terms, 'related': related, 'counts': counts})


def get_count(counter: pd.DataFrame, term: str, word: str):
    ligne = (counter['terms'] == term) & (counter['related'] == word)
    values = counter.loc[ligne, 'counts'].values
    return values[0] if len(values) > 0 else 0


def get_encode(counter: pd.DataFrame, word: str, T: list[str]) -> list[int]:
    return [get_count(counter, term, word) for term in T]


def co_occurence_matrix(configuration: Data, weights, window: int) -> Matrix:
    # We start at position 2 (window of 5)
    # We end up at position (n-1) - 2 (window of 5)
    if window % 2 != 1:
        raise Exception("The window's size should be a odd number")
    side_length = window // 2
    list_of_couples = reduce(lambda x, y: x + y,
                             [get_neighbours(configuration, i, side_length)
                              for i in range(side_length, len(configuration.text) - (1+side_length))])
    counter = create_counter(list_of_couples)
    encodings = np.array([get_encode(counter, word, configuration.T) for word in configuration.B]).T
    df = pd.DataFrame(encodings, columns=configuration.B)
    return PMI(configuration, df) if weights else df


def PCA(matrix: Matrix, T: list[str]):
    kpca = KernelPCA(n_components=len(T), kernel='rbf')
    X_train = kpca.fit_transform(matrix.iloc[:, 1:])
    return matrix


def get_text(file_name: str) -> str:
    f = open(file_name)
    res = reduce(lambda x, y: x + y, [x.replace("\n", "") for x in f.readlines()])
    f.close()
    return res


def get_datas(file_name: str, fileB: str, fileT: str) -> Data:
    text = preprocess(get_text(file_name))
    B = get_word_set(fileB)  # word vector basis
    T = get_word_set(fileT)  # word for similarity and clustering
    return Data(text, B, T)


def tp1(file_name: str, fileB: str, fileT: str) -> tuple[Plot, Similar]:
    configuration = get_datas(file_name, fileB, fileT)
    point_wise_mutual_information = False
    com = co_occurence_matrix(configuration, weights=point_wise_mutual_information, window=5)
    plot = PCA(com, configuration.T)
    similarities = cosine_similarity(com)  # use the PPMI co-occurence matrix
    return (plot, similarities)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception(f"You should put 3 arguments: the B set, the T set and the text file\n only got: {sys.argv}")

    tp1(sys.argv[1], sys.argv[2], sys.argv[3])

# TODO : check that B.txt  has exactly one word per line, no space and no empty lines
# TODO : create a structure to federate text, B, and T
# TODO : use dataframe for a better piping
