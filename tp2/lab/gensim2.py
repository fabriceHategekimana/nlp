from gensim import corpora, models, similarities

from sklearn.datasets import 

corpus = getData(subset='train', remove=("headers", "footers", "quotes"))
x = corpus.data
x = corpus.target
y_names = corpus.target_names

corpora.Dictionary()  # create a dictionnary with token and their indicies

dic.doc2bow(text)  # bag of word representation

model.TfidfModel(corpus)
model.LsifModel(corpus)  # single decomposition matrix
model.LdaModel(corpus)  # principal component analysis
