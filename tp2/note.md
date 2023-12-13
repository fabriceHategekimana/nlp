You will write two Python scripts that take as input a set of sentences (the attached file) and output the following: 

    Using pre-trained word2vec representations:
       1.1  A plot showing embeddings in a two-dimensional space
       1.2  For each input sentence, the most similar sentence except identical
    Using word2vec vectors that you trained:
       2.1  A plot showing embeddings in a two-dimensional space
       2.2  For each input sentence, the most similar sentence except identical 

It is your task to come up with a method for finding the embeddings of the sentences starting from the word2vec embeddings. It is also your task to find an appropriate corpus for training word2vec in the settings in 2. To find the most similar sentences, we calculate cosine similarity between all input sentences and then search the similarity matrix to find the highest value for each given sentence.

## gensim library

This is the library for both loading pre-trained and training new word2vec vectors. To solve this task, you need to find the most appropriate values for the configuration parameters. 

## t-SNE for plotting

This is a non-linear dimensionality reduction algorithm available as a sklearn function. Use sentence IDs as the names for the data points. 

## Evaluation, baseline and leader board

We will evaluate only the settings 1.2 and 2.2. As the baseline, we will use a string similarity score (still to be decided). Your goal should be to outperform this baseline. We will rank your submissions according to the setting 2.2. The winner will get a small prize, but the ranking on the leader board will not impact the grading. 

## Specific requirements

All four outputs should be saved as files. Name the text file outputs like this: out1.2.txt and out2.2.txt. 
The format of these files should be two tab separated columns. The first column: input sentence ID, the second column: the ID of the most similar sentence. Make sure that there is nothing else in out1.2.txt and out2.2.txt.
 
## Clarifications after the Q&A session

Corpus for training word2vec

    There are many ways to obtain a corpus of English plain text. You can search the internet for available resources. Here is, for instance, one that I would use: https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-2735. There are also tools in gensim to create a Wiki corpus. If you know of any more convenient way to find and download a corpus, feel free to use it. 
 

## Same sentence IDs in the given test set
    Sentences with the same IDs should be the most similar ones, but don't expect a 100% match. Since the IDs in the input file are not unique, you might need to use your own unique IDs while calculating similarity, but you need to use the given IDs in the output.   
 

## Types of sentence embeddings
    There are constraints here: 
    you are not allowed to use doc2vec, you need to start with word-level embeddings
    you are not allowed to use BERT-based models 

 

## String similarity as a baseline 
    This is something that should not be part of your submitted code, but you can calculate on the side the following score for all pairs of sentences just to have an idea of what a baseline score would be: 

Dices coefficient = (2*Common Terms) / (Number of terms in String1 + Number of terms in String2)

 
What to submit
    Script 1 named load_tp2.py
    Script 2 named train_tp2.py
    out1.2.txt
    out2.2.txt
    README.txt containing the following (and in this order)
    1. instructions for running your scripts
    2. running time for both scripts 
    3. all non-default gensim parameter settings for both scripts
    4. a brief description of the method used for obtaining sentence embeddings
    5. a brief description of the choice of the training corpus

	
T_sent.txt T_sent.txt
3 novembre 2023, 09:11
