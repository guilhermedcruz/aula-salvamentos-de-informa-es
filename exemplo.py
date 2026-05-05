import os
from dataclasses import dataclass

os.system("cls")


@dataclass
class Funcionario:
    nome:str
    idade: int

    def mostrar_dados(self):
        
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')

Quantidade_Funcionarios = 2
lista_funcionario = []

print('= Solicitando dados =')
for i in range(Quantidade_Funcionarios):
    novo_funcionario = Funcionario(
        nome = input('Digite seu nome: '),
        idade =int(input('Digite sua idade: '))
    )
    print('')
    lista_funcionario.append(novo_funcionario)

print('= Exibindo dados =')
for funcionario in lista_funcionario:
    funcionario.mostrar_dados()
#with serve pra guarda os comandos.
#as serve pra criar um atalho ao a varivel
print('= Salvando dados =')
with open('lista_funcionarios.csv', 'a', encoding='utf-8') as arquivo:
    for funcionario in lista_funcionario:
        arquivo.write(f"{funcionario.nome}, {funcionario.idade}")
        print('Salvo com sucesso!')