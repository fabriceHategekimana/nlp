import gensim.downloader as api


def compute_model(model):
    print(wv.most_similar(positive=["car"], topn=1))


if __name__ == '__main__':
    wv = api.load("glove-twitter-24")
    compute_model(wv)
