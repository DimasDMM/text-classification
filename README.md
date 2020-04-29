# Text classification

## Introduction

Text classification is an interesting topic in the NLP field. In this repository, you will find an overview of different algorithms to use for this purpose.

> To use this repository, you will need to use **Docker** and, if you want to use the commands described below, you will need to be in a **Unix** platform (since they use Bash scripts). Additionally, to open the notebooks, you should have already installed **Jupyter notebooks** in your computer. Finally, we have used different Python libraries that are listed here: [requirements.txt](./misc/dockerfiles/python/requirements.txt)

## Dataset

I have used a dataset which consists of 2225 documents from the BBC news website corresponding to stories in five topical areas from 2004-2005. These documents are classified in 5 different categories: business, entertainment, politics, sport, tech.

Source: http://mlg.ucd.ie/datasets/bbc.html - D. Greene and P. Cunningham. "Practical Solutions to the Problem of Diagonal Dominance in Kernel Document Clustering", Proc. ICML 2006.

## Notebooks

I have split the repository in several notebooks:
- [Data Analysis and Preprocess](./notebooks/Data-Analysis-and-Preprocess.ipynb)
- [Training with LSTM](./notebooks/Training-with-LSTM.ipynb) - A simplified version is available at [Kaggle](https://www.kaggle.com/dimasmunoz/simple-text-classification-with-lstm).
- [Training with SVM](./notebooks/Training-with-SVM.ipynb) - A simplified version is available at [Kaggle](https://www.kaggle.com/dimasmunoz/simple-text-classification-with-svm).

> **Important**: The LSTM model uses pre-trained vectors from the Glove project. If you want to use that model, first you must download the set `GloVe 6B` and place the file `glove.6B.100d.txt` in the path `./data/glove.6B/glove.6B.100d.txt`. See https://nlp.stanford.edu/projects/glove/

## Commands

> Note: These commands have been tested in MacOS

You can control the docker containers with these two commands:
```sh
sh manager.sh docker:run
sh manager.sh docker:down
```

Now, you have two commands that you can use to train the model and to make predictions:
```sh
sh manager.sh train
sh manager.sh predict "Write your text here..."
```

And one additional command to enter to the Python container:
```sh
sh manager.sh python
```

For example, let's make a prediction:
```sh
$ sh manager.sh predict "A text about tennis"
INFO:root:Applying char cleaner...
INFO:root:Applying lemmatization...
INFO:root:Loading model "svm"...
sport
```

Have fun! ᕙ (° ~ ° ~)
