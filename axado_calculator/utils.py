#!/usr/bin/python3
# -*- coding: utf8 -*-
# Este arquivo é responável por mantar os métodos estáticos utilizados para facilitar algumas
# tarefas, deixando o código de "bussines" mais limpo e coerente. além de manter o padrao "S" da arquiterura S.O.L.I.D.
#

# imports baseados em http://docs.python-guide.org/en/latest/writing/style/#code-style

# system import
import csv
import logging
# project import
import exceptions


def get_row_by_weight_range(column, column_value, start, end, value, file_name, dialect=None):
    """
    Metodo Responsável por abrir o arquivo com os dados da rota e varificar se o valor esta dentro
    da min e max determinados.
    A declaração com "with" é melhor porque ele irá garantir que você sempre fechar o arquivo, mesmo
    se uma exceção for levantada dentro do bloco.

    :param column:string
    :param column_value:string
    :param start:string
    :param end:string
    :param value:string
    :param file_name:string
    :param dialect:none
    :return: raw:dict
    """
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        if dialect:
            reader = csv.DictReader(csvfile, dialect=dialect)
        for row in reader:
            if row[end]:
                if row[column] == column_value:
                    if float(row[start]) <= value < float(row[end]):
                        return row
            else:
                if row[column] == column_value:
                    return row

def get_route(origem_a, destino_a, origem_b, destino_b, file_name, file_type):
    """
    Metodo responsável por abrir o arquivo de acordo com seu tipo e verificar
    se a origem e destino estão corretos.
    A declaração com "with" é melhor porque ele irá garantir que você sempre fechar o arquivo, mesmo
    se uma exceção for levantada dentro do bloco.

    :param origem_a:string
    :param destino_a:string
    :param origem_b:string
    :param destino_b:string
    :param file_name:string
    :return: row:dict
    """
    with open(file_name) as csvfile:
        if file_type == 'csv':
            reader = csv.DictReader(csvfile)
        else:
            reader = csv.DictReader(csvfile, dialect='excel-tab')
        for row in reader:
            if row[origem_a] == origem_b and row[destino_a] == destino_b:
                return row

        raise exceptions.RouteNotFound("Rota não encontrada.")
