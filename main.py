combustivel = ['Gasolina', 5.90, 'Etanol', 4.89, 'Diesel', 7.89]
login = []
senha = []
bd = []
#Entrada de Dados
print('Qual o Combustível?\n1 - Gasolina\n2 - Etanol\n3 - Diesel')
opcombustivel = input('Opção: ')
#Débito, Dinheiro e Pix desconto - Juros 2% ao mês
print('Qual a forma de pagamento?\n1 - Débito\n2 - Crédito\n3 - Pix\n4 - Dinheiro')
oppagamento = input('Opção: ')
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
print(bd)