#!/usr/bin/python3
# -*- coding: utf8 -*-
# Este arquivo é unicamente responsável por manter as configurações necessárias para o
# funcionamento correto do software, útil quando é preciso fazer deploy continuo usando jenkins, por exemplo, que pode
# fácilmente subscrever estas variáveis de acordo com a finalidade do deploy, seja para staging(maturação de feature),
# homologação(testes) ou produção.
# facilita também a implantação e o controle de "feature flags" e "roll backs"
# respeitando o padrão "S" da arquitetura S.O.L.I.D.
#
# *  S  - Sigle Responsability Principle
#

import os

# Caminho dos diretorios para acesso aos arquivos
PATH_ROTA_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets/tabela/rotas.csv')
PATH_VALOR_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets/tabela/preco_por_kg.csv')
PATH_ROTA_TSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets/tabela2/rotas.tsv')
PATH_VALOR_TSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets/tabela2/preco_por_kg.tsv')

# Configuração para logging da aplicação
PATH_LOGS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs/default.log')
LOG_FORMAT = '[%(asctime)s] - %(message)s'
DATE_LOG_FORMAT = '%m/%d/%Y %I:%M:%S %p'
