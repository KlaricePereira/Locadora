#Essa é uma classe chamada "Titulo", que possui quatro atributos: "id", "nome", "duracao" e "diaria". No método construtor, que é chamado quando um novo objeto é criado, esses atributos são inicializados com valores passados como argumentos.
class Titulo:
    def __init__(self, id, nome, duracao, diaria):
        self._id = id
        self._nome = nome
        self._duracao = duracao
        self._diaria = diaria

    def __str__(self):
        return f'id = {self._id}, nome = {self._nome}, duracao = {self._duracao} diaria =                        {self._diaria}'

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
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, duracao):
        self._duracao = duracao

    @property
    def diaria(self):
        return self._diaria

    @diaria.setter
    def diaria(self, diaria):
        self._diaria = diaria

  

