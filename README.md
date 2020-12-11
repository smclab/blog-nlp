# Blog NLP

In this repository are present some jupyter notebooks and scripts related about Tech Blog Natural
Language Processing articles series.

## Repository Organization

This repository is organized in multiple folders. Every folder is related to specific article in Smc Tech Blog.

* [1-ner](1-ner): contains code related to Named Entity Recognition article
* [2-text-classification](): coming soon
* [3-topic-modeling](): coming soon
* [4-entity-linking](): coming soon
* [5-machine-translation](): coming soon

## Execution in Docker Environment

All code is executable in Docker environment. There is a Docker Compose file that build an image based
on Tensorflow with Jupyter Notebook integrated. (See Dockerfile inside nlp folder)
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

Just launched the container you can see on logs the url to log into jupyter notebook environment.
Copy url that begins with *http://127.0.0.1:8888/?token=* and paste it on your browser. 
Then go to *http://localhost:8888* and run notebooks.

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


