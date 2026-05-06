import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Catalogo:
    nome: str
    autor: str
    categoria: str
    preco: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Autor: {self.autor}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço: {self.preco}\n")


lista_catalogo = []

while True:
    print("""
============== Catalogo de livro ================
       opção 1: Adicionar livro
       opção 2: Listar livros
       opção 3: Sair do Catalogo
""")

    opcao = int(input("Insira uma opção: "))

    if opcao == 1:
        print('= Solicitando dados sobre o Livro =')

        novo_livro = Catalogo(
            nome=input("Digite o nome do livro: "),
            autor=input("Digite o nome do autor: "),
            categoria=input('Digite a categoria do livro: '),
            preco=input("Digite o preço do livro: ")
        )

        lista_catalogo.append(novo_livro)

        print('= Salvando dados do livro =')
        with open('Catalogo_livros.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{novo_livro.nome},{novo_livro.autor},{novo_livro.categoria},{novo_livro.preco}\n")

        print('Livro salvo com sucesso')

    elif opcao == 2:
        lista_catalogo = []

        with open('Catalogo_livros.csv', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome, autor, categoria, preco = linha.strip().split(',')
                livro = Catalogo(nome, autor, categoria, preco)
                lista_catalogo.append(livro)

        for livro in lista_catalogo:
            livro.mostrar_dados()

    elif opcao == 3:
        print('Saindo...')
        break

    else:
        print('Opção inválida, tente outra.')