# apirest_ativ2
 



Pierre Fernandes Brandão







Atividade 2 da Disciplina:
 Arquitetura de Serviços



Prof.ª Leonardo Guerreiro Azevedo














Rio de Janeiro
Julho de 2022
 


1.	Introdução

O objetivo deste trabalho é implementar um serviço RESTFul de consulta de dados. Seré utilizado a linguagem Python e o Framework Django Rest.   

2.	Conceito

O serviço RESTFul são princípios arquiteturais para implementação de uma API REST.

2.1	Definição API e API REST.

API ou interface de programação de aplicações são protocolos e restrições no desenvolvimento de integrações de aplicações. Uma API REST é uma API que está em conformidade com a arquitetura REST. Esta arquitetura foi criada por Roy Fielding em 2000

3.	Princípios RESTful
•	Arquitetura Cliente/Servidor com solicitações gerenciadas por HTTP.
o	São utilizados métodos HTTP, como GET, POST para comunicação.
•	Comunicação stateless, ou seja, não existe informação das transações anteriores, cada nova transação é feita do zero.
•	Expor as URLs com uma estrutura tipo diretório.
•	Transferência por XML, Json ou ambos. 

4.	Diferenças entre SOAP e REST

O REST surgiu após o SOAP e costuma ser visto como uma alternativa mais rápida para comunicação Web. Suas principais diferenças são:
•	REST é um conjunto de diretrizes com implementação flexível.
•	SOAP é um protocolo com requisitos específicos.
•	REST tem mais de um tipo de mensageria, como o XML, JSON, HTML, etc.
•	SOAP usa somente o XML.



5.	Conclusão
Devido a arquitetura REST ser mais flexível e aceitar mais de um formato, ela é mais fácil para implementação.
Também não encontrei um framework SOAP para a linguagem Python que ofereça as mesmas funcionalidades que o framework Django REST, portanto seria necessário desenvolver.



6.	Prática
Foi utilizado o Framework Python DJango REST para implementação do projeto.

6.1	Arquitetura 
O Django utiliza arquitetura MVT (Model, View, Template), onde o model é o mapeamento do banco de dados, no View é implementada a lógica do negócio e o Template são as páginas para visualização dos dados. Este modelo é similar ao padrão MVC


 

6.2	Modelo de dados

 


7.	Referências
•	Richardson, L. and Ruby, S. “RESTful web services”, O'Reilly Media, Inc., 2011
•	O que é API REST, https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api#rest, consultado em 17/07/2022

•	Architectural Styles and the Design of Network-based Software Architectures, https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm, consultado em 17/07/2022

•	Introduction to RESTful Web services, https://developer.ibm.com/articles/ws-restful/, consultado em 17/07/2022

•	Django REST framework, https://www.django-rest-framework.org/, consultado em 17/07/2022


