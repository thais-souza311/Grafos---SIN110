def saida(inst, rows, cols):

# abertura de arquivo para escrita
    armazena = open('Lista1/SaidaDados/resultado.txt', 'a+')

# escreve a instancia, linha e coluna no arquivo
    armazena.write(inst + str(rows) + str(cols) + '\n')
# print que aparecera na tela
    print(inst + ' ' + str(rows) + ' ' + str(cols) + '\n')
# fecha arquivo
    armazena.close

    return rows, cols