combustivel = ['Gasolina', 5.90, 'Etanol', 4.89, 'Diesel', 7.89]
pagamento = ['Débito', 'Crédito', 'PIX', 'Dinheiro']
login = senha = bd = []
opcombustivel = ' '
while True:
#Entrada de Dados
    while True:
        print('Qual o Combustível?\n1 - Gasolina\n2 - Etanol\n3 - Diesel')
        opcombustivel = input('Opção: ')
        if opcombustivel not in '123':
            print('Opção inválida')
        else:
            break
            
    while True:
    #Débito, Dinheiro e Pix desconto - Juros 2% ao mês
        print('Qual a forma de pagamento?\n1 - Débito\n2 - Crédito\n3 - Pix\n4 - Dinheiro')
        oppagamento = input('Opção: ')
        if oppagamento not in '1234':
            print('Opção inválida')
        else:
            break
    qtdlitros = float(input('Qual a quantidade de litros?\nLitros: '))

    if oppagamento in '134':
        porcentagemv = float(input('Qual a % de desconto?\n'))
        if opcombustivel == 1:
            total = combustivel[1] * qtdlitros
        elif opcombustivel == 2:
            total = combustivel[3] * qtdlitros
        else:
            total = combustivel[5] * qtdlitros
        venda = total - (total * (porcentagemv / 100))
        vendatotal = print(f'Venda Total de:\nR$ {venda:.2f}')
    if oppagamento in '2':
        qtdparcelas = int(input('Quantidade de parcelas?\n'))
        porcentagemj = 0.05
        if opcombustivel == 1:
            total = combustivel[1] * qtdlitros
        elif opcombustivel == 2:
            total = combustivel[3] * qtdlitros
        else:
            total = combustivel[5] * qtdlitros

        venda = total + (total * (porcentagemj * qtdparcelas))
        print(f'Venda Realizada\nRecibo')
        vendatotal = print(f'Venda Total de:\nR$ {venda:.2f}')

    def gerarid(bd):
        count = 0
        while True:
            if count not in bd:
                return count
            count += 1
    bd.append(gerarid(bd))
    bd.append(pagamento[int(oppagamento)-1])
    if oppagamento in '2':
        bd.append(int(qtdparcelas))
    else:
        bd.append(0)
    bd.append()
    continuar = str(input('Você deseja continuar? (S/N)\n')).upper()
    if continuar in 'N':
        break
print(bd)