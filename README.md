# Blog NLP

In this repository are present some jupyter notebooks and scripts related about Tech Blog Natural
Language Processing articles series.

## Repository Organization

This repository is organized in multiple folders. Every folder is related to specific article in Smc Tech Blog.

* [1-ner](nlp/1-ner): contains code related to [Named Entity Recognition article](https://techblog.smc.it/en/2020-12-11/nlp-ner)
* [2-text-classification](nlp/2-text-clf): contains code related to [Text Classification](https://techblog.smc.it/en/2020-12-21/nlp-text-clf)
using Machine Learning
* [3-topic-modeling](nlp/3-topic-modelling): contains code related to [Topic Modelling con Gensim](https://techblog.smc.it/en/2021-10-15/topic-modelling)
* [4-entity-linking](): coming soon
* [5-machine-translation](): coming soon

## Execution in Docker Environment

All code is executable in Docker environment. There is a Docker Compose file that build an image based on [Tensorflow with Jupyter Notebook integrated](https://hub.docker.com/r/tensorflow/tensorflow/tags?page=1). (See Dockerfile inside nlp folder)
The image contains also some default notebooks provided by tensorflow for some simple tutorials.

Inside nlp folder are presente the directiories for every task based on repository organization.

To build and run the container execute:

```shell
docker-compose up -d
```

You can see logs of servive typing:

```shell
docker-compose logs -f nlp
```
Below is an example of logs obtained from the previous command. From the logs 
you can see the link to access the Jupyter Notebooks. Copy url that begins with *http://localhost:8888/?token=* and paste it on your browser. 

```shell
nlp  | [I 12:30:11.008 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
nlp  | [I 12:30:11.278 NotebookApp] Serving notebooks from local directory: /tf
nlp  | [I 12:30:11.278 NotebookApp] Jupyter Notebook 6.4.3 is running at:
nlp  | [I 12:30:11.278 NotebookApp] http://b5c600697c97:8888/?token=dadecfedb52a32ff30e0b8ed153a5b7076eaf7033e12d5eb
nlp  | [I 12:30:11.278 NotebookApp]  or http://127.0.0.1:8888/?token=dadecfedb52a32ff30e0b8ed153a5b7076eaf7033e12d5eb
nlp  | [I 12:30:11.278 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
nlp  | [C 12:30:11.283 NotebookApp]
nlp  |
nlp  |     To access the notebook, open this file in a browser:
nlp  |         file:///root/.local/share/jupyter/runtime/nbserver-1-open.html
nlp  |     Or copy and paste one of these URLs:
nlp  |         http://b5c600697c97:8888/?token=dadecfedb52a32ff30e0b8ed153a5b7076eaf7033e12d5eb
nlp  |      or http://127.0.0.1:8888/?token=dadecfedb52a32ff30e0b8ed153a5b7076eaf7033e12d5eb
```

To rebuild image type:

```shell
docker-compose build
```

To stop container run:

```shell
docker-compose down
```

The nlp directory is binded as external volumes, so all changes in notebooks inside container 
are saved.


