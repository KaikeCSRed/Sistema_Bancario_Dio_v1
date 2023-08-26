

saldo = 0;
extrato = '';
numeros_saques_diarios = 0
LIMITE = 500;
LIMITE_SAQUES = 3; 


menu = '''
Olá, O que deseja ?
[e] Extrato
[d] Depósito
[s] Saque
[q] Sair \n
'''

while True:
        opcao = input(menu).lower()
        
        if opcao == "e" :
                print(f''' \n Segue seu extrato \n{extrato} \n Saldo Atual : {saldo:.2f}''');
        elif opcao == 'd':
                valor_de_deposito = float(input('Qual Valor deseja depositar ? \n'));
                if(valor_de_deposito > 0):
                         saldo += valor_de_deposito;
                         extrato += f" \n +{valor_de_deposito}"
                         print(f'\nVocê Realizou o Depósito no valor de {valor_de_deposito} \n');   
                else:
                      print('Não foi possível realizar Esse Deposito, Tente Novamente. \n ');           
        elif opcao == 's':
                if (numeros_saques_diarios < LIMITE_SAQUES):
                    valor_de_saque = float(input(f'Qual Valor deseja sacar ? \n'));
                    if(valor_de_saque <= saldo and valor_de_saque > 0):
                        if(valor_de_saque <= LIMITE):
                            sacar = float(input(f'''Confirma o saque no valor de {valor_de_saque:.2f} ?\n[1] = Sim [2] = Não \n'''))
                            if sacar == 1: 
                                    numeros_saques_diarios += 1
                                    saldo -= valor_de_saque
                                    extrato += f" \n -{valor_de_saque:.2f}"
                                    print (f'Você sacou: {valor_de_saque:.2f}')
                            elif sacar == 2:
                                    print("Tudo Bem, Cancelamos a sua solicitação de Depósito")
                        else:
                         print(f"Desculpe o Seu Limite de Saque é de : {LIMITE} \n ")
                    else:
                     print(f'\nSaldo Insuficiente.')
                else:
                     print(f'Desculpe não foi possível Realizar o saque pois você atingiu o limite de {LIMITE_SAQUES} Saques.')
                
        elif opcao == 'q':
            break
        else:
            print('Operação invalida, coloque novamente a operação desejada')