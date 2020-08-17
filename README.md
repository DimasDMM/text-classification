# Text classification

## Introduction

Text classification is an interesting topic in the NLP field. In this repository, you will find an overview of different algorithms to use for this purpose: SVM, LSTM and RoBERTa.

The details of results are in the notebooks:

|              | LSTM   | SVM    | RoBERTa |
|--------------|--------|--------|---------|
| **Accuracy*** | 96.26% | 96.86% | 98.50% |

*These are the top accuracy values that I achieved in my runnings.

## Notebooks

I have split the repository in several notebooks:
- [Data Analysis and Preprocess](./notebooks/Data-Analysis-and-Preprocess.ipynb)
- [Training with LSTM](./notebooks/Training-with-LSTM.ipynb) - See in [Kaggle](https://www.kaggle.com/dimasmunoz/simple-text-classification-with-lstm).
- [Training with SVM](./notebooks/Training-with-SVM.ipynb) - See in [Kaggle](https://www.kaggle.com/dimasmunoz/simple-text-classification-with-svm).
- [Training with RoBERTa](./notebooks/Training-with-RoBERTa.ipynb) - See in [Kaggle](https://www.kaggle.com/dimasmunoz/text-classification-with-roberta-and-tpus).

> **Important**: The LSTM model uses pre-trained vectors from the Glove project. If you want to use that model, first you must download the set `GloVe 6B` and place the file `glove.6B.100d.txt` in the path `./data/glove.6B/glove.6B.100d.txt`. See https://nlp.stanford.edu/projects/glove/

## Dataset

I have used a dataset which consists of 2225 documents from the BBC news website corresponding to stories in five topical areas from 2004-2005. These documents are classified in 5 different categories: business, entertainment, politics, sport, tech.

Source: http://mlg.ucd.ie/datasets/bbc.html - D. Greene and P. Cunningham. "Practical Solutions to the Problem of Diagonal Dominance in Kernel Document Clustering", Proc. ICML 2006.

## Commands

> I tested these commands in MacOS (any Unix platform is good) and Windows (in Git Bash terminal).

I have implemented the necesary code to train **an SVM model** and make predictions. All the code run in docker containers, so you only must install **Docker** in your computer.

You can control the docker containers with these two commands:
```sh
sh manager.sh docker:run
sh manager.sh docker:down
```

Now, you have two commands that you can use to train a model and make predictions:
```sh
sh manager.sh train
sh manager.sh predict "Write your text here..."
```

For example, let's make a prediction:
```sh
$ sh manager.sh predict "A text about tennis"
INFO:root:Applying char cleaner...
INFO:root:Applying lemmatization...
INFO:root:Loading model "svm"...
sport
```

And one additional command to enter (if you need it) to the Python container:
```sh
sh manager.sh python
```

Have fun! ᕙ (° ~ ° ~)
