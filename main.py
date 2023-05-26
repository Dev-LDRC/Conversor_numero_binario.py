from logic import calculo_conversao_binaria, calculo_conversao_decimal #
###########################################################################
positivo = ['S', 'SIM', 'SI'] #############################################
###########################################################################

print ('Olá!')
print('Bem vindo ao nosso programa de\n|- Conversão BINÁRIA e DECÍMAL -|')
print('--------------------------------------')

while True:
    escolha = input('Qual opção você deseja?\n\t( 1 ) | DECÍMAL --> BINÁRIO\n\t( 2 ) | BINÁRIO --> DECÍMAL\n\t'
    '( 000 ) | Sair do programa\n( ? )  -> ')
    print('--------------------------------------')

    if int(escolha) == 1:
        print('DECÍMAL --> BINÁRIO')
        print('Como usar:\n\t- Digite um numero qualquer que você deseje saber o binário.')
        print()

        n_decimal = input('digite um numero -> ')
        result1 = calculo_conversao_decimal(n_decimal)
        print(f'{n_decimal} => ( {result1} )')
        print('|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|')

        while input('Fazer outro calculo? ').upper() in positivo:
            n_decimal = input('digite um numero -> ')
            result1 = calculo_conversao_decimal(n_decimal)
            print(f'{n_decimal} => ( {result1} )')
            print('|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|')
        else:
            print('|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|')
            print()

    if int(escolha) == 2:
        print('BINÁRIO --> DECÍMAL')
        print('Como usar:\n\t- Digite a quantidade de Numeros que você quiser.\n\t- Só pode usar os numeros "0" e "1"\n\t'
        '- Depois de ter digitado, confirme e Espere a conversão terminar e o resultado "decímal" chegar.')
        print()

        n_binario = input('Digite sua sequencia binária -> ')
        result2 = calculo_conversao_binaria(n_binario)
        print(f'{n_binario} => ( {result2} )')
        print('|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|')

        while input('Fazer outro calculo? ').upper() in positivo:
            n_binario = input('Digite sua sequencia binária -> ')
            result2 = calculo_conversao_binaria(n_binario)
            print(f'{n_binario} => ( {result2} )')
            print('|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|')
        else:
            print('|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|')
            print()

    if escolha == '000':
        print('Obrigado por usar nosso programa, até mais... :)')
        break