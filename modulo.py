# importa biblioteca para criação das classes abstratas
from abc import ABC, abstractmethod

# classe abstrata, que irá funcionar como uma interface
class Conta(ABC):
    #interface só possui métodos
    @abstractmethod
    def consultar_saldo(self):
        pass

    @abstractmethod
    def fazer_deposito(self):
        pass

    @abstractmethod
    def fazer_saque(self):
        pass

#subclasse conta corrente
class ContaCorrente(Conta):
    #atributos 
    def __ini__(self, nome, cpf, agencia, conta, saldo):
        self.__nome = nome
        self.__cpf = cpf
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo
        super().__init__()


    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def agencia(self):
        return self.__agencia
    
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def conta(self):
        return self.__conta
    
    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    #método da classe abstrata
    def consultar_saldo(self):
        return self.__saldo

    def fazer_deposito(self,valor):
        self.__saldo += valor
        return self.__saldo

    def fazer_saque(self,valor):
        self.__saldo -= valor
        return self.__saldo 

