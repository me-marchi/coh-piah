import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve
    uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print()

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista
    contendo cada texto como um elemento'''
    i = 1
    textos = []
    print()
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
     
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do
    texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases
    dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro
    da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de
    palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de
    palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve
    devolver o grau de similaridade nas assinaturas.'''
    x = 0
    soma = 0
    while x < 6:
        f = abs(as_a[x] - as_b[x])
        soma = f + soma
        x = x + 1
    similaridade = soma/6
    return similaridade


def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a
    assinatura do texto.'''
    # Número total de sentenças
    lista_sentencas = separa_sentencas(texto)

    # Soma dos caracteres por sentença
    x = 0
    caracteres_sentenca = 0
    while x < len(lista_sentencas):
        caracteres_sentenca = len(lista_sentencas[x]) + caracteres_sentenca
        x = x + 1
        
    # Número total de frases
    x = 0
    lista_frases = []
    while x < len(lista_sentencas):
        frases = separa_frases(lista_sentencas[x])
        y = 0
        while y < len(frases):
            lista_frases.append(frases[y])
            y = y + 1
        x = x + 1

    #Soma dos caracteres por frase
    x = 0
    caracteres_frase = 0
    while x < len(lista_frases):
        caracteres_frase = len(lista_frases[x]) + caracteres_frase
        x = x + 1

    # Número total de palavras
    x = 0
    lista_palavras = []
    while x < len(lista_frases):
        palavras = separa_palavras(lista_frases[x])
        y = 0
        while y < len(palavras):
            lista_palavras.append(palavras[y])
            y = y + 1
        x = x + 1
         
    # Número total de caracteres
    x = 0
    lista_caracteres = []
    while x < len(lista_palavras):
        caracteres = lista_palavras[x]
        c = list(caracteres)
        y = 0
        while y < len(c):
            lista_caracteres.append(c[y])
            y = y + 1
        x = x + 1

        
    palavras_unicas = n_palavras_unicas(lista_palavras)
    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    
    media_palavras = (len(lista_caracteres))/(len(lista_palavras))
    type_token = (palavras_diferentes)/(len(lista_palavras))
    hapax_legomana = (palavras_unicas)/(len(lista_palavras))
    media_sentenca = (caracteres_sentenca)/(len(lista_sentencas))
    complexidade_sentenca = (len(lista_frases))/(len(lista_sentencas))
    media_frase = (caracteres_frase)/(len(lista_frases))
    
    as_a = [media_palavras,type_token,hapax_legomana,media_sentenca,
            complexidade_sentenca,media_frase]
    return as_a



def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma
    assinatura ass_cp e deve devolver o numero (1 a n) do texto com
    maior probabilidade de ter sido infectado por COH-PIAH.'''
    n = 0
    autores = []
    while n < len(textos):
        assinatura_a = calcula_assinatura(textos[n])
        co_similaridade = compara_assinatura(assinatura_a, ass_cp)
        n = n + 1
        autores.append(co_similaridade)
    i = 1
    minimo = autores[0]
    autor = 0
    while i < len(autores):
        if autores[i] < minimo:
            minimo = autores[i]
            autor = i + 1
        else:
            autor = autor + 0
        i = i + 1
    if minimo == autores[0]:
        autor = 1
    print('O autor do texto',autor,'está infectado com COH-PIAH')
    return autor


assinaturas = [4.325, 0.7375, 0.5875, 54.125, 2.0, 26.5625]
lista_textos = ["Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.", "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.", "Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens."]
avalia_textos(lista_textos, assinaturas)
