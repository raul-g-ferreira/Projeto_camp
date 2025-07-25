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
    pontuacao: int

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

def processa_clubes(jogos: list[Jogo]) -> list[Clube]:
    '''
    Processa uma lista de jogos e retorna uma lista de clubes.
    Cada clube é representado por um objeto da classe Clube.
    A lista de clubes é formada a partir dos jogos processados.
    Exemplo:
    >>> jogos = processa_jogos(['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1'])
    >>> clubes = processa_clubes(jogos)
    >>> clubes[0].nome
    'Sao-Paulo'
    >>> clubes[0].jogos_totais
    1
    >>> clubes[0].wins
    0
    >>> clubes[0].draws
    0
    >>> clubes[0].gols_totais
    1
    >>> clubes[0].jogos_anf
    1
    >>> clubes[0].wins_anf
    0
    >>> clubes[0].gols_anf
    1
    >>> clubes[0].gols_tomados
    2
    >>> clubes[0].saldo
    -1
    '''
    
    clubes: list[Clube] = []
    
    for jogo in jogos:
        idx_anf = verifica_nome(jogo.anf, clubes)
        idx_visit = verifica_nome(jogo.visit, clubes)
        # se o clube anfitriao não estiver na lista
        if idx_anf == -1:
            tomados = jogo.gols_visit
            gols_totais = jogo.gols_anf
            clube_anf = Clube(nome=jogo.anf,
                              jogos_totais = 1,
                              wins = 1 if jogo.gols_anf > jogo.gols_visit else 0,
                              draws = 1 if jogo.gols_anf == jogo.gols_visit else 0,
                              gols_totais = jogo.gols_anf,
                              jogos_anf = 1,
                              wins_anf = 1 if jogo.gols_anf > jogo.gols_visit else 0,
                              gols_anf = jogo.gols_anf,
                              gols_tomados = tomados,
                              saldo = gols_totais - tomados,
                              pontuacao = 0)
            clubes.append(clube_anf)
        else: # O clube anfitrião está na lista
            clube_anf = clubes[idx_anf]
            clube_anf.jogos_totais += 1
            clube_anf.gols_totais += jogo.gols_anf
            clube_anf.jogos_anf += 1
            clube_anf.wins_anf += (jogo.gols_anf > jogo.gols_visit)
            clube_anf.gols_tomados += jogo.gols_visit
            clube_anf.saldo = (clube_anf.gols_totais - clube_anf.gols_tomados)
        
        # se o clube visitante não estiver na lista
        if idx_visit == -1:
            gols_totais = jogo.gols_visit
            tomados = jogo.gols_anf
            clube_visit = Clube(nome = jogo.anf,
                                jogos_totais = 1,
                                wins = 1 if jogo.gols_visit > jogo.gols_anf else 0,
                                draws = 1 if jogo.gols_anf == jogo.gols_visit else 0,
                                gols_totais = jogo.gols_visit,
                                jogos_anf = 0,
                                wins_anf = 0,
                                gols_anf = 0,
                                gols_tomados = tomados,
                                saldo = gols_totais - tomados,
                                pontuacao = 0)
        
        else: # O clube visitante está na lista
            clube_visit = clubes[idx_visit]
            clube_visit.jogos_totais += 1
            clube_visit.gols_totais += jogo.gols_visit
            clube_visit.gols_tomados += jogo.gols_anf
            clube_visit.saldo = clube_visit.gols_totais - clube_visit.gols_tomados
            clube_visit.wins += (jogo.gols_visit > jogo.gols_anf)
            clube_visit.draws += (jogo.gols_visit == jogo.gols_anf)
    return clubes

def pontuacao_clubes(clubes: list[Clube]):
    '''
    Atribui a pontuação aos clubes de *clubes*.
    A pontuação é calculada da seguinte forma:
    - Vitória: +3 pontos
    - Empate: +1 ponto
    - Derrota: 0 pontos
    Sendo armazenada no campo pontuacao de cada clube.
    Exemplo:
    >>> clubes = [Clube('Sao-Paulo', 1, 1, 0, 2, 1, 1, 2, 1, 0), Clube('Flamengo', 1, 0, 1, 1, 0, 0, 0, 1, 0)]
    >>> pontuacao_clubes(clubes)
    >>> clubes[0].pontuacao
    3
    >>> clubes[1].pontuacao
    1
    '''
    for clube in clubes:
        clube.pontuacao += clube.wins * 3
        clube.pontuacao += clube.draws
    # sem return, pois altera o próprio parâmetro!

def em_ordem_alfabetica(clubex: Clube, clubey: Clube) -> bool:
    '''
    Compara dois clubes e retorna True se o nome do clube *clubex* for
    lexicograficamente menor que o nome do clube *clubey*.
    Exemplo:
    >>> Sao_Paulo = Clube('Sao-Paulo', 0, 0, 0, 0, 0, 0, 0, 0, 0)
    >>> Flamengo = Clube('Flamengo', 0, 0, 0, 0, 0, 0, 0, 0, 0)
    >>> em_ordem_alfabetica(Sao_Paulo, Flamengo)
    True
    >>> em_ordem_alfabetica(Flamengo, Sao_Paulo)
    False
    '''
    return clubex.nome < clubey.nome
def ordena_clubes(clubes: list[Clube]):
    '''
    Ordena *clubes* de acordo com os seguints critérios:
    1. Pontuação
    2. Número de vitórias
    3. Saldo de gols
    4. Ordem alfabética do nome do clube
    Retorna a lista ordenada.
    Exemplo:
    >>> clubes = [Clube('Sao-Paulo', 1, 1, 0, 2, 1, 1, 2, 1, 0), Clube('Flamengo', 1, 0, 1, 1, 0, 0, 0, 1, 0)]
    >>> classificacao(clubes)
    '''
    for i in range(len(clubes) - 1):
        if clubes[i].pontuacao < clubes[i + 1].pontuacao:
            aux = clubes[i]
            clubes[i] = clubes[i + 1]
            clubes[i + 1] = aux
        elif clubes[i].pontuacao == clubes[i+1].pontuacao:
            if clubes[i].wins < clubes[i + 1].wins:
                aux = clubes[i]
                clubes[i] = clubes[i + 1]
                clubes[i + 1] = aux
            elif clubes[i].wins == clubes[i + 1].wins:
                if clubes[i].saldo < clubes[i + 1].saldo:
                    aux = clubes[i]
                    clubes[i] = clubes[i + 1]
                    clubes[i + 1] = aux
                elif clubes[i].saldo == clubes[i + 1].saldo:
                    # Fazer a troca por ordem alfabética
                    if not em_ordem_alfabetica(clubes[i], clubes[i + 1]):
                        aux = clubes[i]
                        clubes[i] = clubes[i + 1]
                        clubes[i + 1] = aux
    
def mostra_classificacao(clubes: list[Clube]):
    '''
    Exibe a classificação dos clubes.
    A classificação é exibida no formato:
    TIME     P  V  S

    Onde TIME é o nome do clube, P é a pontuação, V é o número de vitórias e S é o saldo de gols.
    Os valores de P, V e S devem ser alinhados verticalmente com os valores dos outros clubes.
    Exemplo:
    >>> clubes = [Clube('Sao-Paulo', 1, 1, 0, 2, 1, 1, 2, 1, 0), Clube('Flamengo', 1, 0, 1, 1, 0, 0, 0, 1, 0), Clube('Palmeiras', 1, 0, 1, 1, 0, 0, 0, 1, 0)]
    >>> mostra_classificacao(clubes)
    TIME      P V S
    Sao-Paulo 3 1 1
    Flamengo  1 0 0
    '''
    maior_len = len(clubes[0].nome)
    for clube in clubes:
        if len(clube.nome) > maior_len:
            maior_len = len(clube.nome)
    print("TIME " + (" " * (maior_len - 4)) + "P V  S")
    for clube in clubes:
        if clube.saldo >= 0:
            # print(f"{clube.nome}{' ' * (maior_len - len(clube.nome))} {clube.pontuacao} {clube.wins}  {clube.saldo}")
            print(clube.nome + (' '* (maior_len - len(clube.nome))) + ' ' + str(clube.pontuacao)+ ' ' + str(clube.wins)+ '  ' + str(clube.saldo))
        else:
            # print(f"{clube.nome}{' ' * (maior_len - len(clube.nome))} {clube.pontuacao} {clube.wins} {clube.saldo}")
            print(clube.nome + (' ' * (maior_len - len(clube.nome))) + ' ' + str(clube.pontuacao)+ ' ' + str(clube.wins)+ ' ' + str(clube.saldo))

def max_gols_tomados(clubes: list[Clube]) -> int:
    '''
    Determina o maior número de gols sofridos por um clube.
    Retorna o número de gols sofridos.
    Exemplo:
    >>> clubes = [Clube('Sao-Paulo', 1, 1, 0, 2, 1, 1, 2, 1, 0), Clube('Flamengo', 1, 0, 1, 1, 0, 0, 0, 1, 0)]
    >>> mais_gols_tomados(clubes)
    1
    '''
    max_tomados = clubes[0].gols_tomados
    for clube in clubes:
        if clube.gols_tomados > max_tomados:
            max_tomados = clube.gols_tomados
    return max_tomados

def pior_defesa(clubes: list[Clube]):
    '''
    Imprime o(s) clube(s) com a pior defesa.
    A pior defesa é o clube que tem o maior número de gols sofridos.
    Retorna o nome do clube com a pior defesa.
    Exemplo:
    >>> clubes = [Clube('Sao-Paulo', 1, 1, 0, 2, 1, 1, 2, 1, 0), Clube('Flamengo', 1, 0, 1, 1, 0, 0, 0, 1, 0)]
    >>> pior_defesa(clubes)
    'Flamengo'
    '''
    tomados = max_gols_tomados(clubes)
    pior_defesa: list = []
    for clube in clubes:
        if clube.gols_tomados == tomados:
            pior_defesa.append(clube.nome)
    print('O(s) times com a pior defesa é(são):')
    for clube in pior_defesa:
        print(clube)
    

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
    jogos_processados = processa_jogos(jogos)
    clubes = processa_clubes(jogos_processados)
    pontuacao_clubes(clubes)
    ordena_clubes(clubes)
    mostra_classificacao(clubes)
    # TODO: solução da pergunta 2
    
    # TODO: solução da pergunta 3
    pior_defesa(clubes) #Precisa ser recursiva!!!!!!!!!!!!!!!!!!!

if __name__ == '__main__':
    main()