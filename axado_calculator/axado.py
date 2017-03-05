#!/usr/bin/python3
# -*- coding: utf8 -*-
# Arquivo principal, instancía a classe Calc, executa a aplicação, captura possiveis exceções e loga as atividades.
#
# Objeativo do software:
#
# O programa deve calcular o prazo e preço de frete de acordo com os detalhes definidos
# abaixo, é uma aplicação simples que está relacionada com o trabalho da Axado.
#
# Assinatura​: axado <origem> <destino> <nota_fiscal> <peso>
# Output por tabela: ​<nome da pasta>:<prazo>, <frete calculado>
#
# Exemplo de output:
# $ axado florianopolis brasilia 50 7
# tabela1:3, 104.79
# tabela2:2, 109.05
#

# imports baseados em http://docs.python-guide.org/en/latest/writing/style/#code-style
# system import
import sys
import os
import logging
import re

# project import
import axado_calculator.models as models
import axado_calculator.exceptions as exceptions
import axado_calculator.config as config

# Nome do arquivo de logs, definido nas configurações
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), config.PATH_LOGS)

# Formato do log, definido nas configurações
logging.basicConfig(format=config.LOG_FORMAT,
                    datefmt=config.DATE_LOG_FORMAT,
                    filename=filename,
                    level=logging.INFO)


def main(args):
    """
    Classe principal, entry point da aplicação. responsável por instanciar os objetos e apresentar o resultado dos
    métodos invocados pelos objetos.

    :param args:string <origem> <destino> <nota_fiscal> <peso>
    :return:string <nome da pasta>:<prazo>, <frete calculado>
    """
    try:
        origem, destino, nota_fical, peso = args
        calculadora = models.Calc(origem, destino, int(nota_fical), int(peso))
        prazo_1, valor_1 = calculadora.tabela(1)
        prazo_2, valor_2 = calculadora.tabela(2)
        info = " tabela1: prazo em dias: {}, valor em reais: {} -- tabela2: prazo em dias: {}, valor em reais: {}".\
            format(prazo_1, valor_1, prazo_2, valor_2)
        logging.info(info)
        print(info.split('--')[0] + '\n' + info.split('--')[1])

    except exceptions.RouteNotFound as e:
        logging.error(e)
        print(e)

    except Exception as e:
        logging.error(e)
        print(e)


if __name__ == '__main__':
    """Condição que associa o nome do arquivo com o metodo principal, geralmente fazemos isso quando
    queremos executar o metodo main a partir de um comando.
    Faz uma verificação básica do tipo dos parametros de entrada antes de iniciar o programa,
    os 2 primeiros parametros dever ser strings em lowercase o
    2 últimos devem ser números inteiros e positivos.
    Exibe um help para ajudar autilização do programa."""

    if len(sys.argv) == 5:
        _string = re.compile(r'[a-z]')
        _number = re.compile(r'[0-9]')
        if _string.match(sys.argv[1]) and _string.match(sys.argv[2]) and _number.match(sys.argv[3]) and _number.match(
                sys.argv[4]):
            main(sys.argv[1:])
        else:
            print("\nErro na leitura dos parametros de entrada, tente conforme assinatura abaixo.")
            print("Assinatura​:  axado <origem [a-z]> <destino [a-z]> <nota_fiscal [0-9]> <peso [0-9]>\n")
            sys.exit()
    else:
        print("\nParametros incorretos: {}".format(sys.argv[1:]))
        print("\nAssinatura​: axado <origem> <destino> <nota_fiscal> <peso>\n")
        print("Exemplo de output:")
        print("$ axado florianopolis brasilia 50 7")
        print("tabela1:3, 104.79")
        print("tabela2:2, 109.05\n")
        sys.exit()
