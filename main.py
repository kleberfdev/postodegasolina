combustivel = ["Gasolina", 5.90, "Etanol", 4.89, "Diesel", 7.89]
pagamento = ["Débito", "Crédito", "PIX", "Dinheiro"]
login = senha = bd = []
opcombustivel = " "
while True:
    # Entrada de Dados
    while True:
        print("Qual o Combustível?\n1 - Gasolina\n2 - Etanol\n3 - Diesel")
        opcombustivel = input("Opção: ")
        if opcombustivel not in "123":
            print("Opção inválida")
        else:
            break

    while True:
        # Débito, Dinheiro e Pix desconto - Juros 2% ao mês
        print(
            "Qual a forma de pagamento?\n1 - Débito\n2 - Crédito\n3 - Pix\n4 - Dinheiro"
        )
        oppagamento = input("Opção: ")
        if oppagamento not in "1234":
            print("Opção inválida")
        else:
            break
    qtdlitros = float(input("Qual a quantidade de litros?\nLitros: "))

    if oppagamento in "134":
        porcentagemv = float(input("Qual a % de desconto?\n"))
        if opcombustivel == 1:
            total = combustivel[1] * qtdlitros
            tpcombustivel = combustivel[0]
            vlrcombustivel = combustivel[1]
        elif opcombustivel == 2:
            total = combustivel[3] * qtdlitros
            tpcombustivel = combustivel[2]
            vlrcombustivel = combustivel[3]
        else:
            total = combustivel[5] * qtdlitros
            tpcombustivel = combustivel[4]
            vlrcombustivel = combustivel[5]
        venda = total - (total * (porcentagemv / 100))
        print(f"Venda Total de:\nR$ {venda:.2f}")
    if oppagamento in "2":
        qtdparcelas = int(input("Quantidade de parcelas?\n"))
        porcentagemj = 0.05
        if opcombustivel == 1:
            total = combustivel[1] * qtdlitros
            tpcombustivel = combustivel[0]
            vlrcombustivel = combustivel[1]
        elif opcombustivel == 2:
            total = combustivel[3] * qtdlitros
            tpcombustivel = combustivel[2]
            vlrcombustivel = combustivel[3]
        else:
            total = combustivel[5] * qtdlitros
            tpcombustivel = combustivel[4]
            vlrcombustivel = combustivel[5]

        venda = total + (total * (porcentagemj * qtdparcelas))

    def gerarid(bd):
        count = 1
        while True:
            if count not in bd:
                return count
            count += 1

    bd.append(gerarid(bd))
    id = bd[-1]
    bd.append(pagamento[int(oppagamento) - 1])
    if oppagamento in "2":
        bd.append(int(qtdparcelas))
    else:
        bd.append(0)
    bd.append(tpcombustivel)
    bd.append(vlrcombustivel)
    print(f'{"="*10:<10}Venda Realizada{"="*10:>10}')
    print(f"Recibo: {id}".center(35))
    print(f'{"Pagamento:"} {pagamento[int(oppagamento)-1]}'.center(35))
    if oppagamento in "2":
        print(f"Quantidade de Parcelas: {qtdparcelas}x".center(35))
    print(
        f'{tpcombustivel}: {vlrcombustivel:.2f} x {qtdlitros:>5.2f} {" = R$":>4} {total:8.2f}'
    )
    if oppagamento in "2":
        print(f'{"Juros:":.<28}{porcentagemj * qtdparcelas * 100:>6.2f}%')
    else:
        print(f'{"Desconto:":.<28}{float(porcentagemv):>6.2f}%')
    print(f'{"Subtotal:":.<24}R$ {venda:>8.2f}')

    print(f"=" * 35)

    continuar = str(input("Você deseja continuar? (S/N)\n")).upper()
    if continuar in "N":
        break

print(bd)
