# Sistema de controle de produtos

## Pacotes necessários
 - mysql-connector-python
 - Wtforms
 - flask

## Utilização da API
 - Ao iniciar o objeto da classe 'DataBaseController', devem ser definidos os parâmetros a seguir, que por padrão recebem os seguintes valores caso não especificados:
"user='root', password='root', host='localhost', database='scp'"

 - O método 'create', cria um novo produto
 Parâmetros: 'name, description, price, amount'

  - O método 'delete', remove um produto
 Parâmetros: 'id'

  - O método 'update', atualiza um produto
 Parâmetros: 'id, name, description, price, amount'

   - O método 'search_by_name', procura produtos pelo nome e os retorna
 Parâmetros: 'name'

 - O método 'search_by_id', procura produtos pelo id e os retorna
 Parâmetros: 'id'

  - O método 'get_products', retorna todos produtos presentes no db
 Parâmetros: ''

## Teste
Para executa-lo, além da necessidade da instalação das libs abaixo, também é necessário criar o DB, para isso o arquivo externo chamado 'DataBase.sql'
contém os comandos necessários para tal.
Após isso, para executar bastar enviar o comando 'python app.py' tendo o
cmd neste diretório.

## Sobre
Foi desenvolvido o Web App para vaga de Estágio Backend,
seguindo todos requisitos pedidos e com a adição do Frontend para
complementar a entrega.

### Armazenamento
Como armazenamento foi utilizado o Mysql, para sua gestão foi utilizado
o Mysql Workbench.

### BackEnd
O BackEnd foi desenvolvido com Python e em forma de API visto a sua integração com
outros serviços, ele se encontra na pasta 'API', nele contem as funções
de adição, remoção, atualização e pesquisa de produtos, e também com a
preveção de criação de produtos com nomes idênticos.
Libs usadas no BackEnd:

- mysql-connector-python: Para ser realizada a interação com o DB

### FrontEnd
O FrontEnd foi densenvolvido com Python e com a utilização do Flask,
dentre outros frameworks e libs utilizadas no FrontEnd estão:

- Wtforms:  Para integração de formulários com o Flask
- DBConnector: A API desenvolvida para integração com banco de dados
- Bootstrap: Para incrementação do Frontend, melhorando-o visualmente

#### Autor: Wandreus Caetano Vieira