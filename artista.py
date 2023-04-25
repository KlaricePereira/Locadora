#A classe "Artista" é uma classe que representa um artista de música. Ela possui três atributos: o id do artista, o nome do artista e a quantidade de seguidores do artista.
class Artista:
    def __init__(self, id, nome, seguidores):
        self._id = id
        self._nome = nome
        self._seguidores = seguidores
      

    def __str__(self):
        return f'id = {self._id}, nome = {self._nome}, seguidores = {self._seguidores}'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def seguidores(self):
        return self._seguidores

    @seguidores.setter
    def seguidores(self, seguidores):
        self._seguidores = seguidores



  

