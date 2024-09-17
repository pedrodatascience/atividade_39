import os
from modulo import *
#NOTE:Progama principal
if __name__ == "__main__":
    cc = ContaCorrente()

    #entrada de dados
    cc.nome = input('Informe o nome do titular: ')
    cc.cpf = input('Informe o cpf do titular: ')
    cc.agencia = input('Informe a agencia do titular: ')
    cc.conta = input('Informe a conta do titular: ')
    
    while True:
        #saída de dados
        print(f'Nome: {cc.nome}.')
        print(f'CPF: {cc.cpf}.')
        print(f'Agencia: {cc.agencia}.')
        print(f'Conta: {cc.conta}.')
        print(f'Saldo: {cc.conta}.\n')

        #NOTE: exibe menu
        print('1 - Consultar saldo.')
        print('2 - Fazer depósito.')
        print('3 - Fazer saque.')
        print('4 - Sair do programa.')

        #usuário informa a opção desejada
        opcao = input('Informe a opcao desejada: ')

        os.system('cls')

        match opcao:
            case '1':
                print('Consultar saldo\n')
                print(f'Saldo disponível: R$ {cc.consultar_saldo()}.')
                continue
            case '2':
                valor = float(input('Informe o valor do depósito: R$ ')).replace(',','.')
                if valor > 0:
                    cc.saldo = cc.fazer_deposito(valor)
                    print('Depósito efetuado com sucesso.')
                else:
                    print("Valor inválido.")
                continue
            case '3':
                valor = float(input('Valor do saque: R$ ')).replace(',','.')
                if valor <= cc.saldo:
                    cc.saldo = cc.fazer_saque(valor)
                    print('Saque efetuado com sucesso')
                else:
                    print('Não foi possível efetuar o saque.')
                continue
            case '4':
                print('Programa encerrado.')
                break
            case _:
                print('Opção inválida.')
                continue

    '''
    Completem o programa: o usuário vai informar o nome e o CPF, e o programa informa qual a agência, conta e saldo. E aí
    o usuário vai poder escolher se deseja fazer o saque, depósito ou sair do programa.'''


