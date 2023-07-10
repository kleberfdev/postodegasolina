class Combustivel:
    def __init__(self, tipo, preco):
        self.tipo = tipo
        self.preco = preco


class Venda:
    def __init__(self):
        self.combustiveis = [
            Combustivel("Gasolina", 5.90),
            Combustivel("Etanol", 4.89),
            Combustivel("Diesel", 7.89)
        ]
        self.pagamentos = ["Débito", "Crédito", "PIX", "Dinheiro"]
        self.vendas_realizadas = []

    def realizar_venda(self):
        while True:
            op_combustivel = self.obter_opcao_combustivel()
            op_pagamento = self.obter_opcao_pagamento()
            qtd_litros = float(input("Qual a quantidade de litros?\nLitros: "))

            if op_pagamento in ["1", "3", "4"]:
                porcentagem_desconto = float(input("Qual a % de desconto?\n"))
                combustivel = self.combustiveis[int(op_combustivel) - 1]
                total = combustivel.preco * qtd_litros
                venda = total - (total * (porcentagem_desconto / 100))
                print(f"Venda Total de:\nR$ {venda:.2f}")
            elif op_pagamento == "2":
                qtd_parcelas = int(input("Quantidade de parcelas?\n"))
                porcentagem_juros = 0.05
                combustivel = self.combustiveis[int(op_combustivel) - 1]
                total = combustivel.preco * qtd_litros
                venda = total + (total * (porcentagem_juros * qtd_parcelas))

            venda_data = {
                "id": self.gerar_id(),
                "pagamento": self.pagamentos[int(op_pagamento) - 1],
                "qtd_parcelas": qtd_parcelas if op_pagamento == "2" else 0,
                "tipo_combustivel": combustivel.tipo,
                "preco_combustivel": combustivel.preco,
                "venda_total": venda
            }
            self.vendas_realizadas.append(venda_data)

            print(f'{"="*10:<10}Venda Realizada{"="*10:>10}')
            print(f"Recibo: {venda_data['id']}".center(35))
            print(f'{"Pagamento:"} {venda_data["pagamento"]}'.center(35))
            if op_pagamento == "2":
                print(f"Quantidade de Parcelas: {qtd_parcelas}x".center(35))
            print(
                f'{combustivel.tipo}: {combustivel.preco:.2f} x {qtd_litros:>5.2f} {" = R$":>4} {total:8.2f}'
            )
            if op_pagamento == "2":
                print(f'{"Juros:":.<28}{porcentagem_juros * qtd_parcelas * 100:>6.2f}%')
            else:
                print(f'{"Desconto:":.<28}{float(porcentagem_desconto):>6.2f}%')
            print(f'{"Subtotal:":.<24}R$ {venda:>8.2f}')
            print(f"=" * 35)

            continuar = input("Você deseja continuar? (S/N)\n").upper()
            if continuar == "N":
                break

        print(self.vendas_realizadas)

    def obter_opcao_combustivel(self):
        while True:
            print("Qual o Combustível?")
            for i, combustivel in enumerate(self.combustiveis, start=1):
                print(f"{i} - {combustivel.tipo}")
            opcao = input("Opção: ")
            if opcao not in ["1", "2", "3"]:
                print("Opção inválida")
            else:
                return opcao

    def obter_opcao_pagamento(self):
        while True:
            print("Qual a forma de pagamento?")
            for i, pagamento in enumerate(self.pagamentos, start=1):
                print(f"{i} - {pagamento}")
            opcao = input("Opção: ")
            if opcao not in ["1", "2", "3", "4"]:
                print("Opção inválida")
            else:
                return opcao

    def gerar_id(self):
        return len(self.vendas_realizadas) + 1


venda = Venda()
venda.realizar_venda()
