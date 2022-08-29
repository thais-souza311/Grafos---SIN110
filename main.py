# libs utilizadas
# Thais Danieli Branco de Souza - 2021001228
import EntradaDados as ent
import SaidaDados as exit


if __name__ == '__main__':

# looping que identificara qual arquivo sera aberto 
    for i in range(3):
        if i == 0:
            inst = 'exemplo'

        elif i == 1:
            inst = 'ponte'

        else:
            inst = 'zachary'
# matriz resultante da funcao entrada
        data = ent.criaEntrada(inst)
# armazena as qtd_linhas
        rows = len(data[0])
# armazena as qtd_colunas
        cols = len(data)
# funcao saida
        exit.saida(inst, rows, cols)
