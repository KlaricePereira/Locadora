#Essa é uma classe chamada Usuario, que representa um usuário em um sistema. Ela possui um construtor que recebe seis argumentos: id, nome, cpf, endereco, email, telefone e senha. Esses atributos são inicializados na criação de um objeto dessa classe.
class Usuario:
    def __init__(self, id, nome, cpf, endereco, email, telefone, senha):
        self._id = id
        self._nome = nome
        self._endereco = endereco
        self._email = email
        self._telefone = telefone
        self._senha = senha

    def __str__(self):
        return f'id = {self._id}, nome = {self._nome}, endereco = {self._endereco} email =             {self._email} telefone = {self._telefone} senha = {self._senha}'

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
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._email = endereco

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._id = telefone

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha


