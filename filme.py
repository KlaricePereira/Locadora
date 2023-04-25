#Essa é uma classe chamada "Filme", que herda os atributos e métodos da classe "Titulo". Ela representa um filme, que possui um título, duração, diária, sinopse, artista principal e uma lista de outros artistas que participam do filme.
from titulo import Titulo


class Filme(Titulo):

  def __init__(self, id, nome, duracao, diaria, sinopse_filme,
               artista, lista_artista):
    super().__init__(id, nome, duracao, diaria)
    self._sinopse = sinopse_filme
    self._artista = artista
    self._lista_artista = lista_artista

  def __str__(self):
    lista_artista = []
    for artista in self._lista_artista:
      lista_artista.append(artista.nome)
    return f'id = {self._id}, nome = {self._nome}, duracao = {self._duracao}, diaria = {self._diaria}, sinopse = {self._sinopse}, artista = {self._artista}, lista_artista =                        {lista_artista}'

  @property
  def sinopse(self):
    return self._sinopse

  @sinopse.setter
  def sinopse(self, sinopse_filme):
    self.sinopse = sinopse_filme

  @property
  def artista(self):
    return self._artista

  @artista.setter
  def artista(self, artista):
    self._artista = artista

  @property
  def lista_artista(self):
    return self._lista_artista

  @lista_artista.setter
  def lista_artista(self, lista_artista):
    self._lista_artista = lista_artista
