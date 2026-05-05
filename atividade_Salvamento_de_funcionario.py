import os
from dataclasses import dataclass

os.system("cls")

class Funcionario:
    nome:str
    idade:str
    


    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"idade: {self.idade}")
        

lista_Funcionario = []

with open('lista_funcionarios.csv', 'r') as arquivo:
    for linha in arquivo:
        nome, idade = linha.strip().split('')
       
    lista_Funcionario.append(Funcionario(
        nome=nome,
        idade=idade,
           ))

for empresa in lista_Funcionario:
    empresa.mostrar_dados()