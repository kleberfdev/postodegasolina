from tkinter import Tk, Label, Entry, Button

# Lista para armazenar as vendas
vendas = []

def realizar_venda():
    # Obtém os valores dos campos de entrada
    quantidade = float(entrada_quantidade.get())
    valor_litro = float(entrada_valor_litro.get())
    desconto = float(entrada_desconto.get())

    # Calcula o valor total com desconto
    valor_total = quantidade * valor_litro * (1 - desconto/100)

    # Adiciona a venda à lista
    venda = {
        "quantidade": quantidade,
        "valor_litro": valor_litro,
        "desconto": desconto,
        "valor_total": valor_total
    }
    vendas.append(venda)

    # Limpa os campos de entrada
    entrada_quantidade.delete(0, 'end')
    entrada_valor_litro.delete(0, 'end')
    entrada_desconto.delete(0, 'end')

def mostrar_vendas():
    # Cria uma nova janela para exibir as vendas
    janela_vendas = Tk()
    janela_vendas.title("Vendas Realizadas")

    # Cria rótulo para exibição das vendas
    exibicao_vendas = Label(janela_vendas, text="Lista de vendas:\n", justify="left")
    exibicao_vendas.pack()

    # Exibe as vendas na janela
    for i, venda in enumerate(vendas, 1):
        venda_texto = f"Venda {i}:\n"
        venda_texto += f"Quantidade: {venda['quantidade']} litros\n"
        venda_texto += f"Valor do litro: R${venda['valor_litro']}\n"
        venda_texto += f"Desconto: {venda['desconto']}%\n"
        venda_texto += f"Valor total: R${venda['valor_total']}\n\n"
        exibicao_vendas.config(text=exibicao_vendas.cget("text") + venda_texto)

def salvar_vendas():
    # Salva as informações das vendas em um arquivo
    with open("vendas.txt", "w") as arquivo:
        for venda in vendas:
            arquivo.write(f"Quantidade: {venda['quantidade']} litros\n")
            arquivo.write(f"Valor do litro: R${venda['valor_litro']}\n")
            arquivo.write(f"Desconto: {venda['desconto']}%\n")
            arquivo.write(f"Valor total: R${venda['valor_total']}\n\n")

# Cria a janela principal
janela = Tk()
janela.title("Sistema de Posto de Gasolina")

# Cria rótulos e campos de entrada
Label(janela, text="Quantidade de combustível (litros):").grid(row=0, column=0, sticky="w")
entrada_quantidade = Entry(janela)
entrada_quantidade.grid(row=0, column=1)

Label(janela, text="Valor do litro de combustível:").grid(row=1, column=0, sticky="w")
entrada_valor_litro = Entry(janela)
entrada_valor_litro.grid(row=1, column=1)

Label(janela, text="Desconto (%):").grid(row=2, column=0, sticky="w")
entrada_desconto = Entry(janela)
entrada_desconto.grid(row=2, column=1)

# Cria botões para realizar venda, mostrar vendas e salvar vendas
botao_venda = Button(janela, text="Realizar Venda", command=realizar_venda)
botao_venda.grid(row=3, column=0, columnspan=2)

botao_mostrar_vendas = Button(janela, text="Mostrar Vendas", command=mostrar_vendas)
botao_mostrar_vendas.grid(row=4, column=0, columnspan=2)

botao_salvar_vendas = Button(janela, text="Salvar Vendas", command=salvar_vendas)
botao_salvar_vendas.grid(row=5, column=0, columnspan=2)

# Inicia a janela principal
janela.mainloop()
