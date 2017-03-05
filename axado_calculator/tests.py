#!/usr/bin/python3
# -*- coding: utf8 -*-

import unittest
import models
import config
import utils
import os

PATH_ROTA_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), config.PATH_ROTA_CSV)
PATH_ROTA_TSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), config.PATH_ROTA_TSV)
PATH_VALOR_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), config.PATH_VALOR_CSV)
PATH_VALOR_TSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), config.PATH_VALOR_TSV)


class CalcTest(unittest.TestCase):
    def test_get_route_csv(self):
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
        frete = models.Calc('florianopolis', 'brasilia', 50, 7)
        result = frete.get_route_by_file_name(PATH_ROTA_CSV, 'csv')
        self.assertEqual(result, {'origem': 'florianopolis', 'fixa': '13', 'seguro': '3', 'prazo': '3', 'kg': 'flo',
                                  'destino': 'brasilia'})

    def test_get_route_tsv(self):
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
        frete = models.Calc('florianopolis', 'brasilia', 50, 7)
        result = frete.get_route_by_file_name(PATH_ROTA_TSV, 'tsv')
        self.assertEqual(result,
                         {'destino': 'brasilia', 'prazo': '2', 'icms': '6', 'limite': '0', 'origem': 'florianopolis',
                          'seguro': '2', 'alfandega': '0', 'kg': 'flo'})

    def test_get_route_by_file_name(self):
        """
        Repasse de responsabilidade para o metodo de retorno, apenas para manter uma arquitetura menos acoplada.

        :param file_name:string
        :return: row:dict
        """
        self.assertEqual(utils.get_route(
            'origem', 'destino', 'florianopolis', 'brasilia', PATH_ROTA_CSV, 'csv'),
            {'destino': 'brasilia', 'prazo': '3', 'seguro': '3', 'kg': 'flo', 'origem': 'florianopolis', 'fixa': '13'})

    def test_get_price_by_kg(self):
        """
        Metodo responsavel por apresentar o valor do preco do frete, baseado em seu peso e um kg passado por parametro.

        :param kg:string
        :return price:float
        """
        self.assertEqual(float(utils.get_row_by_weight_range('nome', 'flo', 'inicial', 'final', 7,
                                                             PATH_VALOR_CSV)['preco']), 12)

    def test_get_tsv_price_by_kg(self):
        """
        Metodos que pesquisa o valor na tabela2 baseado em kilograma.

        :param kg:string
        :return price:float
        """
        self.assertEqual(float(utils.get_row_by_weight_range('nome', 'flo', 'inicial', 'final', 7,
                                                             PATH_VALOR_TSV, dialect='excel-tab')['preco']),14.5)

    def test_seguro(self):
        """ Calcula valor do seguro baseado na nota fiscal.

        :param seguro:string
        :return seguro:float
        """
        frete = models.Calc('florianopolis', 'brasilia', 50, 7)
        self.assertEqual(frete.seguro(2), 1.0)
        self.assertEqual(frete.seguro(3), 1.5)


    def test_total(self):
        """
        Metodo estatico para formatar a saida do valor total.

        :param sub_total:float
        :param icms:int
        :return total:float
        """
        frete = models.Calc('florianopolis', 'brasilia', 50, 7)
        self.assertEqual(frete.total(98.5, 6), 104.79)
        self.assertEqual(frete.total(102.5, 6), 109.05)

    def test_tabela_1(self):
        """
        Calcula o subtotal e retorna o prazo e o valor total do frete baseado no Id da tabela.

        :param table_id:integer
        :return <prazo:integer>, <total:float>
        """
        frete = models.Calc('florianopolis', 'brasilia', 50, 7)
        rota = frete.get_route_by_file_name(PATH_ROTA_CSV, 'csv')
        table_kg_faixa = frete.get_price_by_kg(rota['kg'])
        subtotal = frete.seguro(rota['seguro']) + int(rota['fixa']) + 7 * int(table_kg_faixa)
        total = frete.total(subtotal, 6)
        self.assertEqual(int(rota['prazo']), 3)
        self.assertEqual(total, 104.79)

    def test_tabela_2(self):
        """
        Calcula o subtotal e retorna o prazo e o valor total do frete baseado no Id da tabela.

        :param table_id:integer
        :return <prazo:integer>, <total:float>
        """
        frete = models.Calc('florianopolis', 'brasilia', 50, 7)
        rota = frete.get_route_by_file_name(PATH_ROTA_TSV, 'tsv')
        if 0 < int(rota['limite']) < frete.peso:
            return "-", "-"

        preco = frete.get_tsv_price_by_kg(rota['kg'])
        seguro = frete.seguro(rota['seguro'])
        faixa = int(frete.peso) * preco
        subtotal = seguro + faixa
        if rota['alfandega'] != '0':
            subtotal *= (int(rota['alfandega']) / 100)
        total = frete.total(subtotal, int(rota['icms']))
        self.assertEqual(int(rota['prazo']), 2)
        self.assertEqual(total, 109.05)

if __name__ == '__main__':
    unittest.main()
