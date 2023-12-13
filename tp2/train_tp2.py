from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
from gensim.models.keyedvectors import KeyedVectors
from functools import reduce


def preprocess_text(line):
    return simple_preprocess(line.replace("\n", ""))


def create_and_train_model(file_name):
    f = open(file_name)
    tokens = reduce(lambda x, y: x + y,
                    [preprocess_text(line) for line in f.readlines()])
    f.close()
    model = Word2Vec([tokens], vector_size=100, window=5, min_count=1, workers=4)
    model.wv.save("trained_model.kv")
    return model


def load_local_model(file_name):
    loaded_model = KeyedVectors.load(file_name)
    print(loaded_model.most_similar("hat", topn=2))


if __name__ == '__main__':
    model = create_and_train_model("T_sent.txt")
