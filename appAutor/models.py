from typing_extensions import Self
from django.db import models
from django.forms import CharField

# Create your models here.
class Pais(models.Model):
    def __init__(self, id_pais,sigla,nome):              
        self.id_pais=id_pais
        self.sigla=sigla
        self.nome=nome

    @property    
    def id_pais(self):
        return self._id_pais
    def sigla(self):
        return self._sigla
    def nome(self):
        return self._nome

   
    def id_pais(self, value):
        self._id_pais = value

  
    def sigla(self, value):
        self._sigla = value
  
    def nome(self, value):
        self._nome = value


class Estado(models.Model):
    def __init__(self,id_estado,sigla,nome):             
        self.id_estado=id_estado
        self.sigla=sigla
        self.nome=nome

    @property    
    def id_estado(self):
        return self._id_estado
    def sigla(self):
        return self._sigla
    def nome(self):
        return self._nome

    
    def id_estado(self, value):
        self._id_estdo = value
    
    def sigla(self, value):
        self._sigla = value
    
    def nome(self, value):
        self._nome = value


class Cidade(models.Model):
    def __init__(self,id_cidade,nome):               
        self.id_cidade=id_cidade   
        self.nome=nome
    @property    
    def id_cidade(self):
        return self._id_cidade
    def nome(self):
        return self._nome

    
    def id_cidade(self, value):
        self._id_cidade = value

    
    def nome(self, value):
        self._nome = value


class Endereco(models.Model):
    def __init__(self, id_endereco,cep,logradouro,numero,complemento):  
        self.id_endereco=id_endereco           
        self.cep=cep
        self.logradouro=logradouro
        self.numero=numero
        self.complemento=complemento
        
    @property    
    def id_endereco(self):
        return self._id_endereco
    def cep(self):
        return self._cep
    def logradouro(self):
        return self._logradouro
    def numero(self):
        return self._numero
    def complemento(self):
        return self._complemento
    def cidade(self):
        return self.__class__.cidade
    def estado(self):
        return self.__class__.estado
    def pais(self):
        return self.__class__.pais
    
    
    def id_endereco(self,value):
        self._id_endereco = value
    
    
    def cep(self,value):
        self._cep = value
    
    
    def logradouro(self,value):
        self._logradouro = value
    
    
    def numero(self,value):
        self._numero = value
    
    
    def complemento(self,value):
        self._complemento = value
    
    
    def cidade(self,id_cidade,nome):
        self.cidade = Cidade(id_cidade,nome)
    
    
    def estado(self,id_estado,sigla,nome):
        self.estado= Estado(id_estado,sigla,nome)
    
    
    def pais(self,id_pais,sigla,nome):
        self.pais = Pais(id_pais,sigla,nome) 
  
   

class Autor(models.Model):

    cpf=models.CharField(max_length=11)
    nome=models.CharField(max_length=260)
    datanascimento=models.CharField(max_length=10)
    endereco = Endereco
    endereco.id_endereco(endereco,models.IntegerField())
    endereco.cep(endereco,models.CharField(max_length=9))
    endereco.logradouro(endereco,models.CharField(max_length=260))
    endereco.numero(endereco,models.IntegerField())
    endereco.complemento(endereco,models.CharField(max_length=160))
    endereco.cidade(endereco,models.IntegerField(),models.TextField(max_length=160))
    endereco.estado(endereco,models.IntegerField(),models.TextField(max_length=2),models.TextField(max_length=160))
    endereco.pais(endereco,models.IntegerField(),models.TextField(max_length=3),models.TextField(max_length=160))
    feito = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)





