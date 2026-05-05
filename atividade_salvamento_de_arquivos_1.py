import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class empresa:
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
        nova_empresa = empresa(
            nome = input('Digite o nome da empresa: '),
            cnpj =int(input('Digite o CNPJ da empresa:  ')),
            telefone =int(input('Digite o telefone da empresa: '))
        )
        print('')
        lista_empresas.append(nova_empresa)

print('= Exibindo dados =')
for empresa in lista_empresas:
     empresa.mostrar_dados()
print('= Salvando dados =')
with open('Contato_Empresas.csv', 'a', encoding='utf-8') as arquivo:
     for empresa in lista_empresas:
          arquivo.write(f"{empresa.nome}, {empresa.cnpj}, {empresa.telefone}")
          print('Contato de empresa salvo com sucesso')