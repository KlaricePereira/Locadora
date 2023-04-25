#A classe Album herda de Titulo e representa um álbum de música. Ele tem atributos adicionais, como o número de faixas e os artistas que participaram da gravação. O construtor da classe inicializa esses atributos, juntamente com os atributos herdados de Titulo.

from titulo import Titulo

class Album(Titulo):

    def __init__(self, id, nome, duracao, diaria, faixa, artistas):
        super().__init__(id, nome, duracao, diaria)
        self._n_faixa = faixa
        self._artistas = artistas
      
#O método __str__() retorna uma representação em string dos atributos do objeto.
    def __str__(self):
        return f'id = {self._id}, nome = {self._nome}, duracao = {self._duracao} diaria =                         {self._diaria} faixa = {self._faixa} diaria = {self._diaria}'

#Os métodos @property e @setter são usados para definir e obter o número de faixas e os artistas.
    @property
    def n_faixa(self):
        return self._faixa

    @n_faixa.setter 
    def n_faixa(self, faixa):
        self.faixa = faixa

    @property
    def artistas(self):
        return self._artistas

    @artistas.setter
    def artistas(self, artistas):
        self._artistas = artistas

  