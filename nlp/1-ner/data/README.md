# Data for training

In this directory you can find data related with dataset [Annotated Corpus for Named Entity Recognition
](https://www.kaggle.com/abhinavwalia95/entity-annotated-corpus?select=ner_dataset.csv) from Kaggle.

In particular the dataset is present in three different format.

* [iob scheme](iob_ner_dataset.csv): not used in notebooks but you can use this in place
of biluo dataset in [bilstm ner notebook](../notebooks/bilstm%20ner.ipynb)
* [biluo scheme](biluo_ner_dataset.csv): used in [bilstm ner notebook](../notebooks/bilstm%20ner.ipynb)
* [jsonl scheme](ner_jsonò_dataset.pickle): used in [spacy ner notebook](../notebooks/spacy%20ner.ipynb)

In this directory you can find also a notebook with code to transform dataset from a format to another.
In particular you can transform dataset from iob to biluo scheme, from biluo scheme to jsonl format and
vice versa.