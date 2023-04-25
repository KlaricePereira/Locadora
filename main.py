#importa as classes necessárias: Usuario, Filme, Artista, FormaPagamento e Locacao.
from usuario import Usuario
from filme import Filme
from artista import Artista
from formaPagamento import FormaPagamento
from locacao import Locacao

#Cria instâncias dessas classes para preencher informações sobre os usuários, filmes, artistas, formas de pagamento e locações.
if __name__ == '__main__':

  joao = Usuario(1, 'João', 65764345654, 'Rua 30 de Dezembro', 'joao@gmail',
67643974378, 123)
  maria = Usuario(2, 'Maria', 67865897657, 'sc 434, km04', 'maria@gamil',
677896546, 456)
  julia = Usuario(3, 'Julia', 67864798957, 'Rua Carlos Nauck', 'julia@gamil', 677896546, 876)

  Eric_Darnell = Artista(1, 'Eric Darnell', 20200)
  Carlos_Saldanha = Artista(2, 'Carlos Saldanha', 30400)

  madagascar = Filme(1, 'Madagascar', 96, 3, Eric_Darnell, 'Quatro animais do Zoológico do Central Park que inesperadamente se encontram presos em Madagascar e precisam aprender a se adaptar à natureza.', [Eric_Darnell])
  rio = Filme(2, 'rio', 86, 2,'Capturada por contrabandistas de animais quando tinha acabado de nascer, a arara Blu nunca aprendeu a voar e vive uma vida domesticada feliz em Minnesota, nos Estados Unidos, com sua dona, Linda.', Carlos_Saldanha, [Carlos_Saldanha])
  Os_Pinguins_de_Madagascar = Filme(3, 'Os Pinguins de Madagascar', 92, 5 , Eric_Darnell, 'Os valentes pinguins Capitão, Kowalski, Rico e Recruta se unem a uma força de elite, chamada Vento do Norte, para impedir que o vilão Dr. Octavius Brine acabe com os pinguins do mundo todo.', [Eric_Darnell])

  locacao = Locacao(1, joao, rio, FormaPagamento.CREDITO, 6)
  locacao_2 = Locacao(2, joao, madagascar, FormaPagamento.CREDITO, 2)
  locacao_3 = Locacao(3, maria, rio, FormaPagamento.DEBITO, 8)
  locacao_4 = Locacao(4, julia, madagascar, FormaPagamento.PAYPAL, 5)
  locacao_5 = Locacao(5, julia, rio, FormaPagamento.CREDITO, 4)
  
#Usa o conceito de "lista" para armazenar os objetos criados para cada categoria, como lista_filme, lista_artista e lista_locacao.
  lista_filme = [rio, madagascar, Os_Pinguins_de_Madagascar]
  lista_artista = [Eric_Darnell, Carlos_Saldanha]
  lista_locacao = [locacao, locacao_2, locacao_3, locacao_4, locacao_5]

#Usa laços de repetição para iterar sobre essas listas e extrair informações específicas.
  lista_filmes_alocados = []
  total_joao = 0

#Total de locações de um usuário.
  for locacao in lista_locacao:
    if joao.id == locacao.cliente.id:
      total_joao += locacao.get_valor_locacao()
      lista_filmes_alocados.append(locacao.titulo.nome)

  lista_de_filmes = ''
  for filme in lista_filmes_alocados:
    lista_de_filmes = lista_de_filmes + '\n' + filme

#Valor arrecadado do filme Rio.
  total_filme = 0
  for locacao in lista_locacao:
    if locacao.titulo.id == rio.id:
      total_filme += locacao.get_valor_locacao()

#Mostra os filmes de Eric Darnell
  lista_filme_artista = []
  for filme in lista_filme:
    for artista in filme.lista_artista:
      if Eric_Darnell.id == artista.id:
        lista_filme_artista.append(filme.nome)

  filmes_artista_participou = ''
  for filme in lista_filme_artista:
    filmes_artista_participou = filmes_artista_participou + "\n" + filme

#Exibe a lista de filmes locados por um usuário específico, os filmes em que um artista específico participou, soma das locações de um usuário específico e a receita gerada por um filme específico.
print(f'João locou: {lista_de_filmes}\n')
print(f'Os filmes de Eric Darnell são: {filmes_artista_participou}\n')
print(f'A soma das locações de João é: {total_joao}\n')
print(f'o filme rio arrecadou: {total_filme}\n')



 