import tkinter as tk

root = tk.Tk()

root.geometry("800x450") 
root.title("Controle de Estoque")

fonte_principal = 'Arial'
tamanho_fonte_botoes = 12
width_botoes = 25
height_botoes = 3

# Janela de cadastro para novos produtos
def abrir_janela_cadastro():
    janela_cadastro = tk.Toplevel(root)
    janela_cadastro.title('Cadastrar novo produto')
    janela_cadastro.geometry("800x450")

    titulo_codigo_produto = tk.Label(janela_cadastro, text="Código do produto:", font=(fonte_principal, 12))
    titulo_codigo_produto.pack(padx=10, pady=10)

    entrada_codigo_produto = tk.Text(janela_cadastro, width=width_botoes, height=1, font=(fonte_principal, tamanho_fonte_botoes))
    entrada_codigo_produto.pack(padx=10)

    titulo_nome_produto = tk.Label(janela_cadastro, text="Nome do produto:", font=(fonte_principal, 12))
    titulo_nome_produto.pack(padx=10, pady=10)

    entrada_nome_produto = tk.Text(janela_cadastro, width=width_botoes, height=2, font=(fonte_principal, tamanho_fonte_botoes))
    entrada_nome_produto.pack(padx=10)

    titulo_preco_produto = tk.Label(janela_cadastro, text="Preço do produto:", font=(fonte_principal, 12))
    titulo_preco_produto.pack(padx=10, pady=10)

    entrada_preco_produto = tk.Text(janela_cadastro, width=width_botoes, height=1, font=(fonte_principal, tamanho_fonte_botoes))
    entrada_preco_produto.pack(padx=10)

    botao_cadastrar_novo_produto = tk.Button(janela_cadastro, text='Confirmar', width=20, height=3, font=(fonte_principal, tamanho_fonte_botoes))
    botao_cadastrar_novo_produto.pack(padx=10, pady=20)

def abrir_janela_entrada_estoque():
    janela_entrada_estoque = tk.Toplevel(root)
    janela_entrada_estoque.title('Dar entrada no estoque')
    janela_entrada_estoque.geometry("800x450")

    titulo_codigo_produto = tk.Label(janela_entrada_estoque, text="Código do produto:", font=(fonte_principal, 12))
    titulo_codigo_produto.pack(padx=10, pady=10)

    entrada_codigo_produto = tk.Text(janela_entrada_estoque, width=width_botoes, height=1, font=(fonte_principal, tamanho_fonte_botoes))
    entrada_codigo_produto.pack(padx=10)

    titulo_quantidade_produto = tk.Label(janela_entrada_estoque, text="Quantidade:", font=(fonte_principal, 12))
    titulo_quantidade_produto.pack(padx=10, pady=10)

    entrada_quantidade_produto = tk.Text(janela_entrada_estoque, width=width_botoes, height=1, font=(fonte_principal, tamanho_fonte_botoes))
    entrada_quantidade_produto.pack(padx=10)

    botao_confirmar_entrada_estoque = tk.Button(janela_entrada_estoque, text='Confirmar', width=20, height=3, font=(fonte_principal, tamanho_fonte_botoes))
    botao_confirmar_entrada_estoque.pack(padx=10, pady=20)

# Tela principal
titulo = tk.Label(root, text="EstokFácil", font=(fonte_principal, 20))
titulo.pack(pady=15)

botao_registrar_novo_produto = tk.Button(root, text='Registrar novo produto', width=width_botoes, height=height_botoes, font=(fonte_principal, tamanho_fonte_botoes), command=abrir_janela_cadastro)
botao_registrar_novo_produto.pack(padx=10, pady=10)

botao_entrada_de_estoque = tk.Button(root, text='Registrar entrada no estoque', width=width_botoes, height=height_botoes, font=(fonte_principal, tamanho_fonte_botoes), command=abrir_janela_entrada_estoque)
botao_entrada_de_estoque.pack(padx=10, pady=10)

botao_gerenciar_estoque = tk.Button(root, text='Gerenciar Estoque', width=width_botoes, height=height_botoes, font=(fonte_principal, tamanho_fonte_botoes))
botao_gerenciar_estoque.pack(padx=10, pady=10)

titulo_inserir_produto = tk.Label(root, text="Registrar venda:", font=(fonte_principal, 12))
titulo_inserir_produto.pack(padx=10, pady=10)

entrada_produto = tk.Text(root, width=width_botoes, height=1, font=(fonte_principal, tamanho_fonte_botoes))
entrada_produto.pack(padx=10)

root.mainloop()
