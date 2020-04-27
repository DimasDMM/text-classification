# Text classification [WIP]

## Introduction

Text classification is an interesting topic in the NLP field. In this repository, you will find an overview of different algorithms to use for this purpose.

> To use this repository, you will need to use **Docker** and, if you want to use the commands described below, you will need to be in a **Unix** platform (since they use Bash scripts). Additionally, to open the notebooks, you should have already installed **Jupyter notebooks** in your computer. Finally, we have used different Python libraries that are listed here: [requirements.txt](./misc/dockerfiles/python/requirements.txt)

## Dataset

I have used a dataset which consists of 2225 documents from the BBC news website corresponding to stories in five topical areas from 2004-2005. These documents are classified in 5 different categories: business, entertainment, politics, sport, tech.

Source: http://mlg.ucd.ie/datasets/bbc.html - D. Greene and P. Cunningham. "Practical Solutions to the Problem of Diagonal Dominance in Kernel Document Clustering", Proc. ICML 2006.

## Notebooks

I have split the repository in several notebooks:
- [Data Analysis and Preprocess](./notebooks/Data-Analysis-and-Preprocess.ipynb)
- [Training with LSTM](./notebooks/Training-with-LSTM.ipynb) - This notebook is also available in [Kaggle](https://www.kaggle.com/dimasmunoz/text-classification-with-lstm).
- [Training with SVM](./notebooks/Training-with-SVM.ipynb)

## Commands

You can control the docker containers with these two commands:
```sh
sh manager.sh docker:run
sh manager.sh docker:down
```

And you can open the Python container with this command:
```sh
sh manager.sh python
```

**WIP**

Have fun! ᕙ (° ~ ° ~)
