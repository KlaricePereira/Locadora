#Essa é uma classe chamada "Locacao" que representa a locação de um título (um filme, um livro, etc.) para um cliente, que é identificado pelo atributo "cliente". A classe possui um construtor que recebe como argumentos o id da locação, o cliente, o título, a forma de pagamento e a quantidade de dias que o título ficará locado. 
class Locacao():
    def __init__(self, id, cliente, titulo, FormaPagamento, dias):
        self._id = id
        self._cliente = cliente
        self._titulo = titulo
        self._dias = dias 

    def __str__(self):
        return f'id = {self._id}, cliente = {self._cliente}, titulo = {self._titulo} formapagamento =                        {self._formapagamento} dias = {self._dias}'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._seguidores = titulo

    @property
    def dias(self):
        return self._dias

    @dias.setter
    def dias(self, dias):
        self._dias = dias

  #"get_valor_locacao", que retorna o valor total da locação, calculado multiplicando a diária do título pelo número de dias locados.
    def get_valor_locacao(self):
      return self._titulo.diaria * self._dias

    

