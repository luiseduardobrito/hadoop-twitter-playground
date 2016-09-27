hadoop-twitter-playground
=========================

Simple project for Twitter trend monitoring for São Paulo 2016 mayor elections. Implemented during the [MC855 (2s2016)](www.ic.unicamp.br/~islene/2s2016-projetos/) course in the [Universidade Estadual de Campinas (UNICAMP)](http://www.ic.unicamp.br/).

It was designed to run over Hadoop's MapReduce, but can the executed locally with the shell scripts provided below.

**Installation**

Clone the repository using git then install its requirements:
```sh
cd mc855-2s2016/
pip install
```

**Running the reporters locally**

To start the crawler reporter:
```sh
./run-crawler <term>
```

The start the streaming reporter:
```sh
# The streamer will remain listening until wait_for_count tweets arrives with the supplied term.
./run-streamer <term> <wait_for_count>
```

The should be something like:
```
$ ./run-crawler.sh seguranca

depmajorolimpio: 0.00
jdoriajr: 0.12
celsorussomanno: 0.15
martaprefeita: 0.15
luizaerundina: 0.59

$ ./run-crawler.sh educacao

depmajorolimpio: 0.00
luizaerundina: 0.04
martaprefeita: 0.04
celsorussomanno: 0.24
jdoriajr: 0.68

$ ./run-crawler.sh saude

depmajorolimpio: 0.00
martaprefeita: 0.10
luizaerundina: 0.21
jdoriajr: 0.26
celsorussomanno: 0.42
```

**References**

- [Yahoo! Hadoop Tutorial](https://developer.yahoo.com/hadoop/tutorial/)
- [Writing an hadoop mapreduce program in python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python)
- [Twitter API Tutorial](https://www.codecademy.com/en/tracks/twitter)
- [hardikvasa/hadoop-mapreduce-examples-python](https://github.com/hardikvasa/hadoop-mapreduce-examples-python)


**Roadmap**

- Bug fixes for special characters in query term
- Streamer: continuously report based on input tweets updating the terminal screen.
- Streamer: set max timeout to wait before generating reports
