import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Pokemon:
    nome:str
    tipagem:str
    level:str
    estado:str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'tipagem: {self.tipagem}')
        print(f"Level: {self.level}")
        print(f"Estado: {self.estado}")

lista_Pokemons = []

while True:
    print("""
========== Bem vindo ao Centro pokemon ===========
                  De Cerulean
          opção 1:Adicionar pokemon
          opção 2: Lista de pokemons
          opção 3: Sair do Site
""")
    opcao = int(input("Insira uma opção: "))

    if opcao == 1:
        print('= Solicitando dados sobre o pokemon =')

        novo_pokemon = Pokemon(
            nome =input("Digite o nome do pokemon: "),
            tipagem =input("Digite a tipagem do pokemon: "),
            level =input("Digite o level do pokemon: "),
            estado =input("Digite o estado do pokemon: ")
        )


        lista_Pokemons.append(novo_pokemon)

        print("= Salvando Dados do Pokemon =")
        with open('Site_Poke_Center.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{novo_pokemon.nome}, {novo_pokemon.tipagem}, {novo_pokemon.level}, {novo_pokemon.estado}')

            print('Pokemon cadastrado')
    elif opcao == 2:
        lista_Pokemons = []

        with open('Site_Poke_Center.csv', 'a', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome, tipagem, level, estado = linha.strip().split(',')
                Pokemons = Pokemon(nome, tipagem, level, estado)
                lista_Pokemons.append(Pokemons)

        for Pokemons in lista_Pokemons:
            Pokemons.mostrar_dados()
    elif opcao == 3:
        print('Desligando!..')
        break

    else:
        print(ValueError)
        
            