import sys
from dataclasses import dataclass

@dataclass
class Clube:
    '''Representa um clube de futebol.'''
    nome: str
    jogos_totais: int
    wins: int
    draws: int
    gols_totais: int
    jogos_anf: int
    wins_anf: int
    gols_anf: int
    gols_tomados: int
    saldo: int

@dataclass
class Jogo:
    '''Representa um jogo de futebol entre dois clubes.'''
    anf: str
    gols_anf: int
    visit: str
    gols_visit: int

def verifica_nome(nome: str, lst:list[Clube]) -> int:
    '''
    Determina o índice de um Clube de nome *nome* em *lst*.
    Retorna -1 caso o clube *nome* não estiver na lista.
    Exemplos:
    >>> Curitiba = Clube('Curitiba', 0, 0, 0, 0, 0, 0, 0, 0, 0)  
    >>> Corinthians = Clube('Corinthians', 0, 0, 0, 0, 0, 0, 0, 0, 0)
  
    >>> times = [Curitiba, Corinthians]
    
    >>> verifica_nome('Sao-Paulo', times)
    -1
    >>> verifica_nome('Curitiba', times)
    0
    >>> verifica_nome('Corinthians', times)
    1
    '''
    i = 0
    idx = -1
    found = False
    while not found and i < len(lst):
        if lst[i].nome == nome:
            found = True
            idx = i
        else:
            i += 1
    return idx


def acha_espaco(s: str) -> list[int]:
    '''
    Devolve uma lista com os indices dos espaços de *s*
    Exemplos:
    >>> acha_espaco('Sao-Paulo 1 Atletico-MG 2')
    [9, 11, 23]
    '''
    indices = []
    for i in range(len(s)):
        if s[i] == ' ':
            indices.append(i)
    return indices


def processa_jogos(jogos: list[str]) -> list[Jogo]:
    '''
    Processa uma lista de jogos e retorna uma lista de jogos.
    Cada jogo é representado por um objeto da classe Jogo.
    A lista de jogos é formada a partir de uma lista de strings, onde cada
    string representa um jogo no formato "Anfitrião Gols Visitante Gols
    Exemplo:
    >>> lista = processa_jogos(['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1'])
    >>> lista[0].nome_anf
    'Sao-Paulo'
    >>> lista[0].gols_anf
    1
    >>> lista[0].nome_visit
    'Atletico-MG'
    >>> lista[0].gols_visit
    2
    >>> lista[1].nome_anf
    'Flamengo'
    >>> lista[1].gols_anf
    2
    >>> lista[1].nome_visit
    'Palmeiras'
    >>> lista[1].gols_visit
    1
    '''
    jogos_p = []
    for jogo in jogos:
        indices = acha_espaco(jogo)


        nome_anf = jogo[:indices[0]]
        gols_anf = int(jogo[indices[0] + 1:indices[1]])
        nome_visit = jogo[indices[1] + 1:indices[2]]
        gols_visit = int(jogo[indices[2] + 1:])
        
        
        jogos_p.append(Jogo(anf=nome_anf, gols_anf=gols_anf, visit=nome_visit, gols_visit=gols_visit))
    return jogos_p


def le_arquivo(nome: str) -> list[str]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento
    representa uma linha.
    Por exemplo, se o conteúdo do arquivo for
    Sao-Paulo 1 Atletico-MG 2
    Flamengo 2 Palmeiras 1
    a resposta produzida é
    [‘Sao-Paulo 1 Atletico-MG 2’, ‘Flamengo 2 Palmeiras 1’]
    '''
    try:
        with open(nome) as f:
            return f.readlines()
        
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)
    jogos = le_arquivo(sys.argv[1])
    # TODO: solução da pergunta 1
    # TODO: solução da pergunta 2
    # TODO: solução da pergunta 3


if __name__ == '__main__':
    main()