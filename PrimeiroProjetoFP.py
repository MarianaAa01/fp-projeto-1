#Primeiro projeto de FP
#Mariana Silva de Carvalho
#109974

def eh_territorio(t):
    """
    eh territorio: universal → booleano
    Esta função recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a um territorio e False caso contrario, sem nunca gerar erro.
    """
    if not (isinstance(t,tuple)):
        return False
    
    #Verifica-se o comprimento do tuplo(número de colunas).
    elif not (len(t)>=1) or not (len(t)<=26):                                                                            
        return False

    #Compara-se os comprimentos de cada subtuplo.
    for i in range(0, len(t)):
        if not (isinstance(t[i],tuple)):
                return False
        elif not (len(t[i]) >=1) or not (len(t[i])<= 99):
                return False
        elif len(t[0]) != len(t[i]):                                                                
            return False
    
    #Verifica-se que os tuplos(número de linhas) terão 99 elementos.
    for subtuplo in t:
        for elemento in subtuplo:
            if elemento not in [0,1]:
                return False
            elif not (isinstance(elemento,int)):
                return False
    return True

def obtem_ultima_intersecao(t):
    """
    obtem ultima intersecao: territorio → intersecao
    Esta função recebe um território e devolve a interseção do extremo superior direito do território.
    """
    if not (isinstance (t, tuple)):
        raise ValueError('Território inválido')
    
    tuplo_novo = ()
    letra= chr(len(t)+64)           #Obtem-se a letra correspondente ao ultimo subtuplo(letra).
    num= len(t[0])          #Obtem-se o número através do comprimento de qualquer tuplo, uma vez que são todos iguais.
    tuplo_novo = tuplo_novo + (letra, num)
    return tuplo_novo

def eh_intersecao(arg):
    """
    eh intersecao: universal → booleano
    Esta função recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a uma interseção e False caso contrário, sem nunca gerar erros.
    """
    if not isinstance(arg,tuple):       #Verifica-se que a interseção é um tuplo.
        return False
    elif len(arg) != 2:     #Verifica-se que a interseção é constituída por dois elementos(uma letra e um número).
        return False
    elif (not isinstance (arg[0], str)) or (not isinstance(arg[1], int)): #Verifica-se que o primeiro elemento(letra) é uma string e que o segundo elemento(numero) é um inteiro.
        return False
    elif len(arg[0])!=1: 
        return False
    elif not (65<=ord(arg[0])<=90) or not (1<= arg[1]<= 99): #Verifica-se que a letra vai de A a Z e que o numero vai de 1 a 99.
        return False    
    else:
        return True
    
def eh_intersecao_valida(t, i):
    """
    eh intersecao valida: territorio x intersecao → booleano
    Esta função recebe um território e uma interseção, e devolve True se a interseção corresponde a uma interseção do território, e False caso contrário
    """
    if not eh_intersecao(i):
        return False
    
    letra= ord(i[0])-64
    numero= i[1]

    if (1 <= letra <= len(t)) and (1 <= numero <= len(t[0])): #Verifica-se que a letra corresponde a alguma das colunas existentes no territorio e que o número corresponde a algum número do território.
        return True
    else:
        return False
    
def eh_intersecao_livre(t, i):
    """
    eh intersecao livre: territorio x intersecao → booleano
    Esta função recebe um território e uma interseção do território, e devolve True se a interseção corresponde a uma interseção livre (não ocupada por montanhas) dentro do território e False caso contrário.
    """
    if not eh_intersecao_valida(t,i):
        return False
    
    letra = ord(i[0])-65
    numero = i[1]-1
    #No território os elemento 1 e 0 correspondem a uma interseção ocupada e livre respetivamente.
    if t[letra][numero] != 1:   #Verifica-se que a interseção da coluna e linha escolhidas é diferente de 1, ou seja, 0 e por isso livre.
        return True
    else:
        return False
    
def obtem_intersecoes_adjacentes(t, i):
    """
    obtem intersecoes adjacentes: territorio x intersecao → tuplo
    Esta função recebe um território e uma interseção do território, e devolve o tuplo formado pelas interseções válidas adjacentes da interseção em ordem de leitura de um território.
    """
    if not eh_intersecao_valida (t, i):
        return False

    letra = ord(i[0])-65
    tuplo_novo=()
    #É sempre necessário verificar que as interseções seguintes são válidas antes de adicionar ao tuplo_novo que vai acumulando as interseções válidas e adjacentes.
    cima = ((chr(letra+65)), (i[1]-1))  #A adjacente em cima encontra-se na mesma coluna e num elemento da linha anterior ao elemento da linha da interseção escolhida.
    if eh_intersecao_valida(t,cima):
        tuplo_novo += (cima,)
    esquerda = ((chr(letra+64)), i[1])  #A adjacente à esquerda encontra-se na coluna anterior e no mesmo elemento da linha da interseção escolhida.
    if eh_intersecao_valida(t,esquerda):
        tuplo_novo += (esquerda, )
    direita = ((chr(letra+66)), i[1])   #A adjacente à direita encontra-se na coluna seguinte e no mesmo elemento da linha da interseção anterior.
    if eh_intersecao_valida(t,direita):
        tuplo_novo += (direita,)
    baixo = ((chr(letra+65)),(i[1]+1))  #A adjacente em baixo encontra-se na mesma coluna e num elemento da linha posterior ao elemento da linha da interseção escolhida.
    if eh_intersecao_valida(t,baixo):
        tuplo_novo += (baixo,)
    return tuplo_novo

def ordena_intersecoes(tup):
    """
    ordena intersecoes: tuplo → tuplo
    Esta função recebe um tuplo de interseções (potencialmente vazio) e devolve um tuplo contendo as mesmas interseções ordenadas de acordo com a ordem de leitura do território.
    """
    return tuple(sorted(tup, key=lambda x: (x[1], x[0])))
        
def territorio_para_str(t):
    """
    Esta função recebe um território e devolve a cadeia de caracteres que o reprensenta (a representação externa ou representação “para os nossos olhos”).
    """
    if not eh_territorio(t):
        raise ValueError('territorio_para_str: argumento invalido')

    numero_de_linhas= len(t[0])
    tabela='  '     #Aqui inicia-se a tabela e vai-se adicionando todas as letras da primeira linha consoante o numero se subtuplos(colunas) do território que é dado.
    ultima_linha='  '   #Aqui inicia-se a ultima linha e vai-se adicionando todas as letras da ultima linha consoante o numero se subtuplos(colunas) do território que é dado.
    resto_da_tabela='' #Aqui inicia-se a parte da meio da tabela onde vai-se adicionando os numeros e os pontos as cruzes consoante o numero das interseções e se são válidas ou não.

    for coluna in range(len(t)):    #Percorre-se o tuplo de coluna a coluna, adicionando-se sempre um espaço e uma letra.
        tabela += ' ' + chr(coluna+65)
        if coluna == len(t):
            tabela = tabela 
    tabela += '\n'              #No final troca-se de linha.
    
    while numero_de_linhas>0:
        if len(str(numero_de_linhas)) < 2:          #Verifica-se o numero de dígitos de um número e caso o número tenha apenas um dígito acrescenta-se um espaço inicialmente(com o objetivo de alinhar a tabela).
            resto_da_tabela += ' ' + f'{numero_de_linhas}'
        else:
            resto_da_tabela += f'{numero_de_linhas}'
            
        for elemento in t:              #Verifica-se se a interseção é livre('.') ou ocupada('X') e adiciona-se consoante esses parâmetros e comparando com o território dado.
            if elemento[numero_de_linhas-1]==0:
                resto_da_tabela += ' .'
            else:
                resto_da_tabela += ' X'
        if len(str(numero_de_linhas)) < 2:      #No final de cada linha da tabela é necessário acrescentar um espaço antes de um número com um dígito com o objetivo de alinhar a tabela.
            resto_da_tabela += '  ' + f'{numero_de_linhas}' + '\n' #Acrescenta-se um espaço amais pois ao acrescentar pontos e cruzes os espaços encontram-se todos à esquerda.
        else:
            resto_da_tabela += ' ' + f'{numero_de_linhas}' + '\n'
        numero_de_linhas -= 1

    for coluna in range(len(t)):    #No final acrescenta-se uma linha com todas as letras de maneira idêntica à primeira linha.
        ultima_linha += ' ' + chr(coluna+65)
        if coluna == len(t):
            ultima_linha = ultima_linha + '\n' 
    return tabela + resto_da_tabela + ultima_linha

def obtem_cadeia(t, i):
    """
    obtem cadeia: territorio x intersecao → tuplo
    Esta função recebe um território e uma interseção do território (ocupada por uma montanha ou livre), e devolve o tuplo formado por todas as interseções que estão conectadas a essa interseção ordenadas (incluindo a própria interseção) de acordo com a ordem de leitura de um território.
    """
    if not eh_territorio(t) or not eh_intersecao_valida(t, i):
        raise ValueError('obtem_cadeia: argumentos invalidos')

    tuplo_final=(i,) #Tuplo criado para armazenar o resultado final ao longo do ciclo.
    valor= eh_intersecao_livre(t,i)
    lista_temporaria=[i]        #É criada uma lista com o elemento inicial, onde vão ser armazenadas as interseções que ainda não estejam no tuplo final e que sejam iguais à interseção dada(livre ou ocupada).
    while len(lista_temporaria)!=0:     #O ciclo vai correr enquanto não estiver vazio. O mesmo vai percorrer as interseções e verificar se as mesmas se encontram na cadeia.
        for intersecao in obtem_intersecoes_adjacentes(t,lista_temporaria[0]):
            if intersecao not in tuplo_final and eh_intersecao_livre(t,intersecao)==valor:
                lista_temporaria+= [intersecao]
                tuplo_final+= (intersecao,)
        del(lista_temporaria[0])        #O primeiro elemento da lista vai ser sempre eliminado para que o ciclo eventualmente acabe.
    if len(tuplo_final)==1:     #Condição para que se verifique que se o tuplo final tiver apenas uma interseção, essa será a dada e será devolvida pela função.
        return (i,)
    return ordena_intersecoes(tuplo_final)

def obtem_vale(t, i):
    """
    Esta função recebe um território e uma interseção do território ocupada por uma montanha, e devolve o tuplo (potencialmente vazio) formado por todas as interseções que formam parte do vale da montanha da interseção fornecida como argumento ordenadas de acordo à ordem de leitura de um território.
    """
    if not eh_territorio(t) or not eh_intersecao_valida(t,i) or eh_intersecao_livre(t,i):
        raise ValueError('obtem_vale: argumentos invalidos')
    
    tuplo2=()
    valor= eh_intersecao_livre(t,i)     #Esta variável é utilizada para mais tarde verificar se uma interseção é ocupada.
    tuplo_final=()      #Cria-se um tuplo para ir adicionando os elementos necessários para a solução.

    tuplo1=obtem_cadeia(t,i)    #Obtem-se a cadeia onde se encontra a interseção dada.
    for intersecao in tuplo1:   #As interseções são percorridas: caso sejam adjacentes e livres são adicionadas a um tuplo final.
        adjacentes=obtem_intersecoes_adjacentes(t,intersecao)
        for intersecao in adjacentes:
            tuplo2 += (intersecao,)
        for intersecao in tuplo2:
            if eh_intersecao_livre(t,intersecao) != valor and intersecao not in tuplo_final:
                tuplo_final+= (intersecao,)
    return ordena_intersecoes(tuplo_final)      #A função devolve o tuplo final ordenado.

def verifica_conexao(t, i1, i2):
    """
    verifica conexao: territorio x intersecao x-intersecao → booleano
    Esta função recebe um território e duas interseções do território e devolve True se as duas interseções estão conetadas e False caso contrário.
    """
    if not eh_territorio(t) or not eh_intersecao_valida(t,i1) or not eh_intersecao_valida(t,i2):
        raise ValueError('verifica_conexao: argumentos invalidos')

    tuplo_com_a_cadeia= obtem_cadeia(t,i1)  #Obtem-se a cadeia de uma das interseções dadas e após isso a função devolve True se a segunda interseção dada se encontrar na nessa cadeia. 
    if i2 not in tuplo_com_a_cadeia:
        return False
    else:
        return True
    
def calcula_numero_montanhas(t):
    """
    calcula numero montanhas: territorio → int
    Esta função recebe um território e devolve o número de interseções ocupadas por montanhas no território.
    """
    if not eh_territorio(t):
        raise ValueError('calcula_numero_montanhas: argumento invalido')
    
    numero_de_montanhas=0      #Caso um elemento seja igual a 1, significa que corresponde a uma interseção ocupada, consequentemente é adicionado 1 a uma variável(numero_de_montanhas).
    for coluna in t:
        for linha in coluna:
            if linha==1:
                numero_de_montanhas+= 1
    return numero_de_montanhas    #A função devolve a variável que contém o número de montanhas.

def calcula_numero_cadeias_montanhas(t):
    """
    calcula numero cadeias montanhas: territorio → int
    Esta função recebe um território e devolve o número de cadeias de montanhas contidas no território.
    """
    if not eh_territorio(t):
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
    
    numero_de_cadeias=0
    visitados=()        #Cria-se um tuplo para adicionar todas as interseções que não se podem repetir ao verificar se são ocupadas.
    
    for coluna in range(len(t)):        #O elementos do tuplo são percorridos e cada um corresponde a uma interseção.
        for linha in range(len(t[0])):
            intersecao= (chr(coluna+65),linha+1)
            if not eh_intersecao_livre(t,intersecao) and intersecao not in visitados:  #Verifica-se que as interseções são ocupadas e que não estão na mesma cadeia, uma vez que se estaria a adicionar o numero de montanhas em vez do numero de cadeias.
                visitados += obtem_cadeia(t,intersecao)
                numero_de_cadeias+= 1
    return numero_de_cadeias

def calcula_tamanho_vales(t):
    """
    calcula tamanho vales: territorio → int
    Esta função recebe um território e devolve o número total de interseções diferentes que formam todos os vales do território.
    """
    if not eh_territorio(t):
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    cadeias_ocupadas=()     #Cria-se um tuplo vazio, onde vão sendo adicionadas todas as interseções ocupadas.
    vales_finais=()
    
    for coluna in range(len(t)):        #O elementos do tuplo são percorridos e cada um corresponde a uma interseção.
        for linha in range(len(t[0])):
            intersecao= (chr(coluna+65),linha+1)
            if not eh_intersecao_livre(t,intersecao) and intersecao not in cadeias_ocupadas:        #Verifca-se que a interseção é ocupada e se a mesma não se encontra na variável cadeias_de_vales.
                cadeias_ocupadas+= obtem_cadeia(t,intersecao)
                for intersecao_2 in obtem_vale(t,intersecao):       #Todas as interseções da cadeia de vales são percorridas.
                    if intersecao_2 not in vales_finais:
                        vales_finais+= (intersecao_2,)      #São adicionados as interseções livres e que ainda não se encontrem no mesmo tuplo.
    return len(vales_finais)        #A função devolve o comprimento dos vales finais, uma vez que é pretendido o tamanho dos vales e não as interseções que os constituem.
