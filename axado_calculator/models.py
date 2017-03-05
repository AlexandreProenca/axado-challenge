#!/usr/bin/python3
# -*- coding: utf8 -*-
# Este arquivo é unicamente responável por manter os objetos que software utiliza para realizar
# o calculo do frete, respeitando o padrão "S" da arquiterura S.O.L.I.D.
#
# imports baseados em http://docs.python-guide.org/en/latest/writing/style/#code-style


# system import
import os

# project import
import axado_calculator.config as config
import axado_calculator.utils as utils

PATH_VALOR_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), config.PATH_VALOR_CSV)
PATH_VALOR_TSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), config.PATH_VALOR_TSV)

class Calc:
    """
    Classe principal responsável por armazenas e manupular os dados informados pelo usuários.
    Pattern criacional "Builder" O padrão Builder é um padrão de projetos de software comum que é
    usado para encapsular a lógica de construção de um objeto.
    """

    def __init__(self, origem, destino, nota_fiscal, peso):
        """
        Metodo Construtor.

        :param origem:string
        :param destino:string
        :param nota_fiscal:string
        :param peso:string
        :return:object Calc
        """
        self.origem = origem
        self.destino = destino
        self.nota_fiscal = nota_fiscal
        self.peso = peso

    def get_route_by_file_name(self, file_name, file_type):
        """
        Repasse de responsabilidade para o metodo de retorno, apenas para manter uma arquitetura menos acoplada.

        :param file_name:string
        :return: row:dict
        """
        return utils.get_route('origem', 'destino', self.origem, self.destino, file_name, file_type)

    def get_price_by_kg(self, kg):
        """
        Metodo responsavel por apresentar o valor do preco do frete, baseado em seu peso e um kg passado por parametro.

        :param kg:string
        :return price:float
        """
        return utils.get_row_by_weight_range('nome', kg, 'inicial', 'final', self.peso, PATH_VALOR_CSV)['preco']

    def get_tsv_price_by_kg(self, kg):
        """
        Metodos que pesquisa o valor na tabela2 baseado em kilograma.

        :param kg:string
        :return price:float
        """
        return float(utils.get_row_by_weight_range('nome', kg, 'inicial', 'final', self.peso,
                                                   PATH_VALOR_TSV, dialect='excel-tab')['preco'])

    def seguro(self, seguro):
        """
        Calcula valor do seguro baseado na nota fiscal.

        :param seguro:string
        :return seguro:float
        """
        return int(self.nota_fiscal) * int(seguro) / 100

    @staticmethod
    def total(sub_total, icms):
        """
        Metodo estatico para formatar a saida do valor total.

        :param sub_total:float
        :param icms:int
        :return total:float
        """
        total = sub_total / ((100 - icms) / 100)
        return round(total + .005, 2)

    def tabela(self, table_id):
        """
        Calcula o subtotal e retorna o prazo e o valor total do frete baseado no Id da tabela.

        :param table_id:integer
        :return <prazo:integer>, <total:float>
        """

        if table_id == 1:
            rota = self.get_route_by_file_name(config.PATH_ROTA_CSV, 'csv')
            table_kg_faixa = self.get_price_by_kg(rota['kg'])
            subtotal = self.seguro(rota['seguro']) + int(rota['fixa']) + int(self.peso) * int(table_kg_faixa)
            total = self.total(subtotal, 6)
            return int(rota['prazo']), total

        else:
            rota = self.get_route_by_file_name(config.PATH_ROTA_TSV, 'tsv')
            if 0 < int(rota['limite']) < self.peso:
                return "-", "-"

            preco = self.get_tsv_price_by_kg(rota['kg'])
            seguro = self.seguro(rota['seguro'])
            faixa = int(self.peso) * preco
            subtotal = seguro + faixa
            if rota['alfandega'] != '0':
                subtotal *= (int(rota['alfandega']) / 100)
            total = self.total(subtotal, int(rota['icms']))
            return int(rota['prazo']), total
