def organizar_numeros(lista_binarios):
    return [int(x) for x in lista_binarios]

def verificacao_binaria(n_binario):
    for x in n_binario:
        if x in ['0','1']:
            continue
        else:
            return False
    return True

def calculo_conversao_binaria(numero_binario):
    if verificacao_binaria(numero_binario):
        binario_lista = organizar_numeros(numero_binario)
        somatorio_final = []

        y = len(binario_lista) - 1
        for x in binario_lista:
            somatorio_final.append(x*(2**y))
            y -= 1

        return sum(somatorio_final)
    else:
        return 'Você colocou uma LETRA ou um NUMERO Diferente de "0" e "1", TENTE NOVAMENTE.'

#########################################################################################

def verificacao_decimal(n):
    if n.isdigit():
        return True
    else:
        return False

def calculo_conversao_decimal(numero):
    if verificacao_decimal(numero):
        num = int(numero)
        binario = []
        while num*2 >= 2:
            proximo_resto = (num % 2)
            proximo_num = (num // 2)
            num = proximo_num
            binario.append(str(proximo_resto))
        binario.reverse()
        return int(''.join(binario))
    else:
        return 'Você digitou algo diferente de "numeros", TENTE NOVAMENTE.'