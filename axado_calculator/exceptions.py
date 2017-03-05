#!/usr/bin/python3
# -*- coding: utf8 -*-
# É importante conhecer e tratar corretamente as possíveis exceções nos fluxos de execução do software este arquivo
# é unicamente responsável por manter as exceções customizadas, garantindo o tratamento adequado a cada situação.
#


class RouteNotFound(Exception):
    def __init__(self, params):
        self.message = ''.format(params)
