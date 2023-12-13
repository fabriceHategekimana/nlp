import gensim
import pandas as pd


df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})

text = df.a.apply(gensim.utils.simple_preprocess)

model = gensim.models.Word2Vec(
    window=10,
    min_count=2,
    workers=4,
)

model.build_vocab(text, progress_per=1000)

model.train(text, total_examples=model.corpus_count, epochs=model.epochs)

model.save("./word2vec2.model")

model.wv.most_similar("test")
