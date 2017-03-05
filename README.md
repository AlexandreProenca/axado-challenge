#Axado Challenge
[![Badge](https://travis-ci.org/AlexandreProenca/axado-challenge.svg?branch=master)](https://travis-ci.org/AlexandreProenca/axado-challenge "Travis CI")
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e0c035692b134da6a06662397f85de7f)](https://www.codacy.com/app/linuxloco/axado-challenge?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AlexandreProenca/axado-challenge&amp;utm_campaign=Badge_Grade)
[![Badge](https://img.shields.io/pypi/v/axado-challenge.svg)](https://pypi.python.org/pypi/axado-challenge "Pypi")
[![Badge](https://img.shields.io/pypi/dd/axado-challenge.svg)](https://pypi.python.org/pypi/axado-challenge "Pypi")
[![Badge](https://img.shields.io/pypi/pyversions/axado-challenge.svg)](https://pypi.python.org/pypi/axado-challenge "Pypi")
[![Badge](https://img.shields.io/pypi/l/axado-challenge.svg)](https://pypi.python.org/pypi/axado-challenge "Pypi")
[![Badge](https://img.shields.io/pypi/wheel/axado-challenge.svg)](https://pypi.python.org/pypi/axado-challenge "Pypi")
[![Badge](https://img.shields.io/pypi/format/axado-challenge.svg)](https://pypi.python.org/pypi/axado-challenge "Pypi")
[![Badge](https://img.shields.io/pypi/implementation/axado-challenge.svg)](https://pypi.python.org/pypi/axado-challenge "Pypi")
[![Badge](https://img.shields.io/pypi/status/axado-challenge.svg)](https://pypi.python.org/pypi/axado-challenge "Pypi")
[![Badge](https://img.shields.io/badge/portugues--brasil-ok-green.svg)](https://img.shields.io/badge/portugues--brasil-ok-green.svg "Livechat")
-----------

Nesse desafio você deve fazer um programa que calcule o prazo e preço de frete
de acordo com os detalhes definidos nos [reaquisitos]() , é uma aplicação simples que está relacionada

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
    Assinatura​: axado <origem> <destino> <nota_fiscal> <peso>
    Output por tabela: ​<nome da pasta>:<prazo>, <frete calculado>

    Exemplo de output:
    $ axado florianopolis brasilia 50 7
    tabela:3, 104.79
    tabela2:2, 109.05



#Desenvolvimento

###Instalação

`git clone https://github.com/AlexandreProenca/axado-challenge`

###Instalação Segura

    A forma mais segura de instalar esta biblioteca e usando os pacotes: pip e virtualenv

    $ virtualenv myenv -p python3
    $ cd myenv
    $ source bin/activate
    $ mkdir myproject
    $ cd myproject
    $ git clone https://github.com/AlexandreProenca/axado-challenge
    $ cd axado-challenge/axado_calculator
    $ python axado.py florianopolis brasilia 50 7
    

Utilização
----------
    Assinatura​: python3 axado.py <origem> <destino> <nota_fiscal> <peso>
    Output por tabela: ​<nome da pasta>:<prazo>, <frete calculado>

    Exemplo de output:
    $ axado florianopolis brasilia 50 7
    tabela:3, 104.79
    tabela2:2, 109.05



####Arquitetura
A escolha de uma arquitetura baseada em composição e não em herança,
visando maior coesão e baixo acoplamento, este projeto seguiu as boas
praticas contidas em http://docs.python-guide.org/en/latest/

####Patterns utilizados
O padrão de projeto Builder faz parte de um grupo de padrões intitulado
como criacionais.
O objetivo dessa pattern é simplificar o processo de construção de um
objeto complexo, normalmente especificando somente as características da
instância.

####Testes
Cobertura de 100% no fluxo principal, todos os métodos estão sendo testados
com valores prefixados no intuito de verificar se a logica por tras do
métodos estarão sempre funcionando, não foram cobertos de testes os
fluxos de execução alternativos, pois o eles poderiam se estender muito,
atrapalhando o objetivo do desafio.
A ferramenta utilizada para rodar os teste é o Tox, ele levanta um
ambiente virtual executa os testes e destrói o ambiente além de ter
varias outras opções bacanas como controle de dependências para os
testes, etc..
Para rodar os testes basta digitar tox na raiz do projeto.

####Logging
Como é muito importante poder ter uma rastreabilidade na execução da
aplicação, o projeto está configurado para logar todos as exceptions
e consultas realizadas.
Estes logs podem posteriormente serem coletados por serviços Saas de
terceiros, como logstash, por exemplo, facilitando o rastreamento
de bug e eventos.

####Dependencias
Este projeto roda apenas na versão **3.5 do python**, porém não possui
dependências de bibliotecas externas para ser executado, foram usados
apenas os métodos built-in da linguagem, porém para desenvolvimento
existem algumas dependências para organização e testes do projeto.

####Deploy
O deploy está utilizando os repositórios públicos do pypi.python.org,

####Integração Contínua
O processo de integração contínua esta sendo feito através do serviço
TravisCI, funciona executando os testes e fazendo deploy automático caso
configurado para isso, eu normalmente utilizo as tags para publicar
novas releases e hotfix automaticamente.

####Versionamento GIT
O projeto foi todo desenvolvido em uma branch paralela chamada 'development'
assim é possível acompanhar a evolução do desenvolvimento através dos commits,
as alterações entrar na master através de pull requests e os commits são
pequenos em geral.

####Segurança
Como o projeto envolve apenas execução local e em linha de comando,
tem maior segurança se comparado com sistemas distribuídos e on-line,
porém nada garante que algum dia possa surgir um exploit para alguma
versão da linguagem,ou de alguma biblioteca utilizada, vale sempre ficar
atento aos alertas de segurança.

####Performance
A performance em parte é responsável pela boa experiência que um usuário tem
usando uma aplicação, por isso busquei otimizar o uso de loops e
chamadas de métodos desnecessárias.

###Compatibilidade e ambiente
Python 3.5
  
####Estrutura do pacote

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


##Author
`Axado Challenge` was written by `Alexandre Proença <alexandre.proenca@hotmail.com.br>`
