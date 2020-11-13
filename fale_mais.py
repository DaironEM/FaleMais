# coding=utf-8

class FaleMais:
    relacao_origem_destino = [('011', '016', 1.90),
                              ('016', '011', 2.90),
                              ('011', '017', 1.70),
                              ('017', '011', 2.70),
                              ('011', '018', 0.90),
                              ('018', '011', 1.90)]

    tolerancia_planos = {'FaleMais 30': 30, 'FaleMais 60': 60, 'FaleMais 120': 120}

    def __init__(self, origem, destino, duracao, plano):
        self.__tarifa = None
        self.__origem = origem
        self.__destino = destino
        self.__duracao = duracao
        self.__plano = plano
        self.custo_por_minuto()

    @property
    def tarifa(self):
        return self.__tarifa

    def franquia_plano(self):
        return self.tolerancia_planos[self.__plano]

    def custo_por_minuto(self):
        for relacao in self.relacao_origem_destino:
            if relacao[0] == self.__origem and relacao[1] == self.__destino:
                self.__tarifa = relacao[2]

    #Se tarifa for None retorna False
    def ligacao_valida(self):
        return not(self.__tarifa == None)


    def custo_tempo_sem_plano(self):
        return  self.__tarifa * self.__duracao

    def custo_tempo_com_plano(self, franquia):
        return  (self.__tarifa * 1.10) * (self.__duracao - franquia)

    def ligacao_sera_cobrada(self, franquia):
        return franquia <= self.__duracao

    def valor_com_plano(self):
        if self.ligacao_valida():
            valor_final =  self.valor_com_plano_ligacao_valida()
        else:
            valor_final = '-'
        return valor_final

    def valor_com_plano_ligacao_valida(self):
        franquia = self.franquia_plano()
        if self.ligacao_sera_cobrada(franquia):
            valor_final_ligacao_valida = self.formata_valor_final(self.custo_tempo_com_plano(franquia))
        else:
            valor_final_ligacao_valida = '$ 0.00'
        return valor_final_ligacao_valida

    def valor_sem_plano(self):
        if self.ligacao_valida():
            valor_final = self.formata_valor_final(self.custo_tempo_sem_plano())
        else:
            valor_final = '-'
        return valor_final

    def formata_valor_final(self, valor):
        return "$ {:.2f}".format(valor)
