# PROJETO PYTHON: Buscando Filme

> Um programa que retorna dados do filme que o usuário digitar.

  O Sistema deve perguntar para o usuário o nome do filme que ele deseja buscar, assim, o sistema deve
retornar o Nome, Ano, Ator(es), Diretor, Escritor, Gênero, Produtora, Lançamento, País, Linguagem, Tempo e
Avaliação. Se o programa não encontrar o filme, deve retornar uma mensagem.


# Tecnologias Utilizadas
* **_PyCharm;_**
* **_Python 3;_**

# Exemplo de Uso
### Classe
```
class Filme:
    def __init__(self):
        # Pergunta para o usuário.
        self.nome_filme = str(input('Informe o nome do filme(Em Inglês):'))
```
![Classe](https://github.com/ThiagoLozano/Buscando-Filme/blob/master/Screenshot/Classe.PNG)

### Função para a Busca
```
    def BuscarFilme(self):
        # Request da API.
        r = requests.get("http://omdbapi.com/?t={}&apikey=9ad5540a".format(self.nome_filme))
        dados = r.json()

        # Validação.
        while dados['Response'] == 'False':
            # Mensagem de erro.
            print('Erro: Filme não encontrado. Tente Novamente!\n')
            # Pergunta e faz a request da API novamente.
            self.nome_filme = str(input('Informe o nome do filme(Em Inglês):'))
            r = requests.get("http://omdbapi.com/?t={}&apikey=9ad5540a".format(self.nome_filme))
            dados = r.json()
```
![Busca](https://github.com/ThiagoLozano/Buscando-Filme/blob/master/Screenshot/Funcao.PNG)

# Bibliotecas e Configurações

### Biblioteca Python Utilizada

```
import requests
```
![Biblioteca](https://github.com/ThiagoLozano/Buscando-Filme/blob/master/Screenshot/Biblioteca.PNG)

### Configurações

* API: http://www.omdbapi.com/
* Chave para a API: http://www.omdbapi.com/apikey.aspx

* Uso da API __omdbapi__ que tem como retorno um arquivo JSON().
```
http://omdbapi.com/?t=[insira o filme]&apikey=[insira a chave]
```
