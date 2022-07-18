from appAutor.models import Autor

from rest_framework import serializers

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        pais = ['id_pais', 'sigla','nome']
        estado = ['id_estado', 'sigla','nome']
        cidade = ['id_cidade','nome']
        endereco = ['id_endereco','cep','logradouro','numero','complemento',cidade,estado,pais]
        autor = ['id','cpf','nome','datanascimento',endereco]
 
