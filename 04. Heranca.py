'''
Enunciado do Exercício: Herança Empresa de Tecnologica

Você foi contratado para criar um sistema simples de cadastro 
de empresas. Sua tarefa é implementar duas classes em Python
utilizando o conceito de herança:

Requisitos
==========
1. Classe base: Empresa
    A classe Empresa deve conter:

    Atributos:

        nome: nome da empresa

        cnpj: número do CNPJ

        funcionarios: lista de nomes de funcionários (inicialmente vazia)

    Métodos:

        __init__(self, nome, cnpj): construtor

        adicionar_funcionario(self, nome_funcionario): adiciona um nome à lista de funcionários

        exibir_dados(self): mostra nome, CNPJ e quantidade de funcionários

2. Classe filha: EmpresaTecnologica

    A classe EmpresaTecnologica deve herdar da classe Empresa.

    Atributos adicionais:

        tecnologias: lista de tecnologias que a empresa usa

    Métodos adicionais:

        __init__(self, nome, cnpj, tecnologias): deve usar super() para aproveitar o construtor da classe base

        exibir_tecnologias(self): imprime a lista de tecnologias



'''
class Empresa:
    
    #construtor dos objetos da classe    
    def __init__(self,nome,cnpj):
        
        self.nome = nome
        self.cnpj = cnpj
        self.funcionarios = [] #lista
        
    #metodo para adicionar funcionarios
    def adicionar_funcionario(self, nome_funcionario):
        self.funcionarios.append(nome_funcionario)
        print(f'Funcionário: {nome_funcionario} adicionado')
        
    #metodo para exibir os dados da empresa
    def exibir_dados(self):
        print(f'Nome da empresa: {self.nome}')
        print(f'CNPJ: {self.cnpj}')
        print(f'Número de funcionários: {len(self.funcionarios)}')

#classe filha que herda da classe empresa
class EmpresaTecnologia(Empresa):
    
    #construtor da classe filha 
    def __init__(self, nome, cnpj, tecnologias):
        
        #chama o construtor da classe base, o super é usado para acessar metodos ou atributos da classe principal (mãe/pai ou base)
        super().__init__(nome, cnpj)  
        
        #atributo da classe filha
        self.tecnologias = tecnologias
    
    #metodo especifico da classe filha para exibir tecnologias
    def exibir_tecnologias(self):
        print(f'Tecnologias utilizadas pela empresa : {self.nome}')
        
        for tecnologia in self.tecnologias:
            print(f'Tecnologia: {tecnologia}')
            
###### INICIO DO PROGRAMA ######

#abaixo os argumentos para criar os objetos da classe
empresa_tec = EmpresaTecnologia('Inovatech', '12.478.598/0001-89', ['Python','Cloud(nuvem)', 'Inteligência Artificial'])

#adicionar funcionarios
empresa_tec.adicionar_funcionario('Lucas')
empresa_tec.adicionar_funcionario('Juliana')

#exibir os dados da empresa
empresa_tec.exibir_dados()

#exibir as tecnologias usadas pela empresa
empresa_tec.exibir_tecnologias()













































































































