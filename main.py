# Biblioteca.
import requests


# Classe Filme.
class Filme:
    def __init__(self):
        # Pergunta para o usuário.
        self.nome_filme = str(input('Informe o nome do filme(Em Inglês):'))

    # Função que busca o filme.
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
        else:
            # Cria uma exceção
            try:
                # Retorna os dados do Filme/Desenho.
                print('=' * 50)
                print("""Título: {}
Ano: {}
Atores: {}
Director: {}
Escritor: {}
Gênero: {}
Produção: {}
Lançamento: {}
País: {}
Linguagem: {}
Tempo: {}
Avaliação: {}""".format(dados['Title'], dados['Year'], dados['Actors'], dados['Director'],
                        dados['Writer'], dados['Genre'], dados['Production'], dados['Released'],
                        dados['Country'], dados['Language'], dados['Runtime'], dados['imdbRating'], ))
                print('=' * 30)

            # No caso do Filme ou Desenho não possuir uma Produtora.
            except KeyError:
                # Retorna os dados do Filme/Desenho sem a Produtora.
                print('=' * 50)
                print("""Título: {}
Ano: {}
Atores: {}
Director: {}
Escritor: {}
Gênero: {}
Lançamento: {}
País: {}
Linguagem: {}
Tempo: {}
Avaliação: {}""".format(dados['Title'], dados['Year'], dados['Actors'], dados['Director'], dados['Writer'],
                        dados['Genre'], dados['Released'], dados['Country'], dados['Language'], dados['Runtime'],
                        dados['imdbRating'], ))
                print('=' * 30)


# Cria o objeto 'usuário'.
usuario = Filme()
usuario.BuscarFilme()
