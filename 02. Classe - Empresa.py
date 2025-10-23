'''
Enunciado do Exercício: Classe Empresa em Python
================================================

Você foi contratado para desenvolver um sistema 
simples de gerenciamento de empresas em Python. 

Sua tarefa é criar uma classe chamada Empresa com os seguintes requisitos:

    Atributos:
        nome(nome da empresa)

        cnpj(número do CNPJ)

        area_atuacao(área em que a empresa atua, como "Tecnologia", "Comércio", etc.)

        funcionarios(lista de nomes dos funcionários da empresa)

    Métodos:
        __init__(self, nome, cnpj, area_atuacao)

    Inicializa a empresa com os dados informados.

    
'''
# Definindo a classe Empresa

class Empresa:
    
    #construir os objetos 
    def __init__(self,nome,cnpj,area_atuacao):
        
        self.nome = nome
        self.cnpj = cnpj
        self.area_atuacao = area_atuacao
        self.funcionarios = []
        
    #método para adicionar um funcionário a empresa
    def adicionar_funcionario(self,nome_funcionario):
        
        #adiciona o nome a lista de funcionarios
        self.funcionarios.append(nome_funcionario)
        
        #mensagem de confirmação 
        print(f'Funcionário: {nome_funcionario} adicionar com sucesso!')
        
    #metodo para listar todos os funcionários da empresa
    def listar_funcionarios(self):
        print(f'Funcionários da empresa: {self.nome}')
        
        #percorre a lista de funcionarios
        for funcionario in self.funcionarios:
            #exibir o nome do funcionario
            print(f'Nome do funcionário {funcionario}')
            
    #metodo para exibir os dados principais da empresa
    def exibir_dados(self):
        print(f'Nome da Empresa: {self.nome}')
        print(f'CNPJ: {self.cnpj}')
        print(f'Área de atuação: {self.area_atuacao}')
        print(f'Quantidade de funcionários: {len(self.funcionarios)}')
        
        
###### INICIO DO PROGRAMA ######
#1o passo - Local onde o progrma fará a leitura inicial7
#os argumentos abaixo chamam a classe e os metódos

#nesta etapa vamos passar os argumentos para a criação de cada objeto dentro da classe
minha_empresa = Empresa('Tech Solutions', '12.124.009/0001-88', 'Tecnologia')

#adicionar 2 funcionarios
minha_empresa.adicionar_funcionario('Márcia Oliveira Peixoto')
minha_empresa.adicionar_funcionario('Murilo Araujo')

#listar os funcionários da empresa
minha_empresa.listar_funcionarios()

#exibir os dados da empresa
minha_empresa.exibir_dados()























































































