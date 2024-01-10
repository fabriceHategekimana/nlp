### Readings

- Jay Alammar's blog: A Visual Guide to Using BERT for the First Time
- Transformers Notebooks 

The main goal of this assignment is to use transfer learning to improve the NER scores for the same languages and data sets that we used in the previous assignment. As a reminder, these are the data sets at Universal NER https://github.com/UniversalNER

UNER_Portuguese-Bosque 
UNER_Chinese-GSDSIMP
UNER_Swedish-Talbanken
UNER_Serbian-SET
UNER_Slovak-SNK
UNER_Croatian-SET
UNER_English-EWT 
UNER_Danish-DDT

### Baseline 

For each language (data set), we take the baseline result to be those achieved with the CRF model. Use the results in the attached file as the baseline. 

### Improvement 

Transfer learning library 
Use the transformer library to load and fine-tune a pretrained model. Note that this library supports using PyTorch for creating your computation graph. You can choose this option if you are familiar with PyTorch. Otherwise, the Transformers Trainer option might suite you better. 

Pretrained models
Use one of the BERT-based models (encoders). Try to optimise the number of parameters by looking for lighter models. Note that pre-trained models can be multilingual, language-specific or covering a group of languages. 

The task
Write a single script that can be run for each of the data sets above separately by specifying the language as a command line argument. For example, for the first data set, the argument on the command line should be "Portugese". Your script should perform the following:

    load the corresponding pretrained model
    train a NER classifier by fine-tuning the pretrained model on the corresponding train set
    output the comparison report: for each language, the difference between the baseline result and the transfer learning result per label and the overall difference

Improvement criterion
What counts as improvement is a better score than the baseline on at lease one label per language keeping the overall result equal or better than the baseline. (The baseline results will be published soon.)

### Access to the Baobab cluster 

To get access to the UniGe cluser for this task, please send your short name to Lorenzo.

We will probably need to limit your access to a particular day. For now, we are targetting two days: 

Day 1:  5.1.2024
Day 2:  10.1.2024

#### Submit to moodle as ZIP archive: 

- Script named finetune_tp4.py  
- compare_eval.txt containing your comparison report
- README.txt containing the following (and in this order)
	1. instructions for running your script
	2. list of all pre-trained models, for each model specify the name, the type and the number of parameters

Baseline.txt
