#Axado Challenge

[![Badge](https://travis-ci.org/AlexandreProenca/axado-challenge.svg?branch=master)](https://travis-ci.org/AlexandreProenca/axado-challenge "Travis CI")
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e0c035692b134da6a06662397f85de7f)](https://www.codacy.com/app/linuxloco/axado-challenge?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AlexandreProenca/axado-challenge&amp;utm_campaign=Badge_Grade)
-----------

Nesse teste você deve fazer um programa que calcula o prazo e preço de frete
de acordo com os detalhes definidos abaixo, é uma aplicação simples que está relacionada
com o trabalho da Axado.

###Instalação

`$pip install axado-challenge`

###Instalação Segura

    A forma mais segura de instalar esta biblioteca e usando os pacotes: pip e virtualenv

    $ virtualenv myenv -p python3
    $ cd myenv
    $ source bin/activate
    $ mkdir myproject
    $ cd myproject
    $ pip install axado-challenge

Utilização
----------
    Assinatura​: axado.py <origem> <destino> <nota_fiscal> <peso>
    Output por tabela: ​<nome da pasta>:<prazo>, <frete calculado>

    Exemplo de output:
    $ axado.py florianopolis brasilia 50 7
    tabela:3, 104.79
    tabela2:2, 109.05



###Estrutura dp pacote

     .
    ├── AUTHORS.rst
    ├── CONTRIBUTING.md
    ├── LICENSE.rst
    ├── README.md
    ├── axado_calculator
    │   ├── __init__.py
    │   ├── assets
    │   │   ├── README.txt
    │   │   ├── tabela
    │   │   │   ├── preco_por_kg.csv
    │   │   │   └── rotas.csv
    │   │   └── tabela2
    │   │       ├── preco_por_kg.tsv
    │   │       └── rotas.tsv
    │   ├── axado.py
    │   ├── config.py
    │   ├── exceptions.py
    │   ├── logs
    │   │   └── default.log
    │   ├── models.py
    │   ├── tests.py
    │   └── utils.py
    ├── dev-requirements.txt
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    └── tox.ini




###Compatibilidade e ambiente
    Python 3.5


##Author
`Axado Challenge` was written by `Alexandre Proença <alexandre.proenca@hotmail.com.br>`
