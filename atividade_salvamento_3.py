import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Empresa:
    nome: str
    cnpj: int
    telefone: int

    def mostrar_dados(self):

        print(f'Nome: {self.nome}')
        print(f'CNPJ: {self.cnpj}')
        print(f"Telefone: {self.telefone}")
    print('=' * 33 )
    print("Salvando empresa cadastrada ")
    print("=" * 33)

lista_empresas = []

print('= Solicitando dados da empresa =')
for i in range(1):
        nova_empresa = Empresa(
            nome = input('Digite o nome da empresa: '),
            cnpj =int(input('Digite o CNPJ da empresa:  ')),
            telefone =int(input('Digite o telefone da empresa: '))
        )
        print('')
        lista_empresas.append(nova_empresa)

print('= Salvando dados =')
with open('contato_empresas.csv','a', encoding='utf-8') as arquivo:
     for Empresa in lista_empresas:
          arquivo.write(f'{Empresa.nome}, {Empresa.cnpj}, {Empresa.telefone}\n')
          print('salvo com sucesso!')
print("= Consultando arquivo =") 
lista_contatos = []
with open('contato_empresas.csv', 'r') as arquivo:
     for linha in arquivo:
          nome, cnpj, telefone, = linha.strip().split(',')
          lista_empresas.append(Empresa(nome=nome, cnpj=cnpj, telefone=telefone))
for Empresa in lista_contatos:
     Empresa.mostrar_dados()

print('= Fim do programa =')

