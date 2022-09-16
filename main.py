from collections import defaultdict
from collections import Counter


# CONJUNTOS


# se a ordem das posições não importa e não se deve ter repetição
usuarios_machine_learning = {13, 16, 52, 89, 10, 16, 94}
usuarios_web3 = {52, 10, 16, 10}

print(usuarios_web3)
print(usuarios_machine_learning)

# união dos conjuntos através do "ou" |
assistiram = usuarios_web3 | usuarios_machine_learning
print(assistiram)
print("-------------------------------------------")

for usuarios in assistiram:
    print(usuarios)

print("-------------------------------------------")

# intersecção dos dois conjuntos através do "&"
interseccao = usuarios_web3 & usuarios_machine_learning
print(interseccao)
print("-------------------------------------------")

fez_web3_mas_nao_machine_learning = usuarios_web3 - usuarios_machine_learning
print(13 in fez_web3_mas_nao_machine_learning)
print(94 in fez_web3_mas_nao_machine_learning)
print(1002 in fez_web3_mas_nao_machine_learning)
print("-------------------------------------------")

# "ou exclusivo": quem fez web3 mas não fez machine learning, ou o contrário.
print(usuarios_web3 ^ usuarios_machine_learning)
print("-------------------------------------------")

# modificando os conjuntos em tempo real
conjunto1 = {14, 18, 34, 2, 52, 24, 94, 3}
print(conjunto1)
conjunto1.add(89)
print(conjunto1)
print("-------------------------------------------")

# tonarnado o conjunto imutável
conjunto1 = frozenset(conjunto1)
print(type(conjunto1))

print("-------------------------------------------")
# conjunto com texto
meu_texto = {"olá, meu nome é Guilherme"}
print(type(meu_texto))
print(meu_texto)
print("-------------------------------------------")

#DICIONÁRIO

aparicoes = {
    "Guilherme": 1,
    "Gato": 2,
    "nome": 1,
    "animal": 2,
}
print(aparicoes["Guilherme"])
print(aparicoes["animal"])
print("-------------------------------------------")

aparicoes["João"] = 1
print(aparicoes)

del aparicoes["João"]
print(aparicoes)
print("-------------------------------------------")

print("animal" in aparicoes)
print("nome" in aparicoes)

print("-------------------------------------------")

for elemento in aparicoes:
    print(elemento)
print("-------------------------------------------")

for valores in aparicoes.values():
    print(valores)
print("-------------------------------------------")

print(1 in aparicoes.values())
print("-------------------------------------------")

for elementos in aparicoes:
    valor = aparicoes[elementos]
    print(elementos, valor)

print("-------------------------------------------")

for elementos2 in aparicoes.items():
    print(elementos2)
print("-------------------------------------------")

#desempacontando
for chave, valorr in aparicoes.items():
    print(chave, "=", valorr)
print("-------------------------------------------")

#list comprehension
print([f"palavra {keys}" for keys in aparicoes])
print("-------------------------------------------")
meu_texto2 = "Meu nome é Guilherme Meu pai se chama Silvio Minha mãe se chama Sonia"
meu_texto2 = meu_texto2.lower()
print(meu_texto2.split())
print("-------------------------------------------")
for palavra in meu_texto2.split():
    print(palavra)
print("--------------------------------------------")
# contando quantos itens possuem no dicionário
aparicoes1 = {}
for palavras in meu_texto2.split():
    ate_agora = aparicoes1.get(palavras, 0)
    aparicoes1[palavras] = ate_agora + 1
print(aparicoes1)
print("----------------------------------------------------------------------------------------------------")

# contando os itens após importar o defaultdict
aparicoes_default_dict = defaultdict(int)

for palavrass in meu_texto2.split():
    ate_agora = aparicoes_default_dict[palavrass]
    aparicoes_default_dict[palavrass] = ate_agora + 1
print(aparicoes_default_dict)
#refaturando o códifo acima:
for palavrass in meu_texto2.split():
    aparicoes_default_dict[palavrass] += 1
print(aparicoes_default_dict)

print("-----------------------------------------------------------------------------------------------------")

dicionario = defaultdict(int)
print(dicionario['guilherme'])

dicionario['guilherme'] = 15
print(dicionario)

print("-----------------------------------------------------------------------------------------------------")

class Conta:
    def __init__(self):
        print('Criando uma conta')

contas = defaultdict(Conta)

print(contas[15])
print(contas[870909])
print("-----------------------------------------------------------------------------------------------------")

# Conrando os itens após importar o Counter

aparicoes_counter = Counter(meu_texto2.split())
print(aparicoes_counter)
print("-----------------------------------------------------------------------------------------------------")

#Criando um contador de letras e palavras utilizando diversas coleções

texto1 = """A Web 3.0 se refere a uma nova era da Internet: mais descentralizada, menos dependente de big techs e capaz de dar aos usuários o controle sobre seus próprios dados. Na prática, é uma web com código aberto; sem tantos ou nenhum intermediário mediando as conversas dos usuários; com dinheiro eletrônico não controlado pelo Estado; e serviços financeiros antes só ofertados por bancos.

Mas assim como o metaverso, utopia futurista que busca unir o real e o virtual, a Web 3.0 ainda está construção.

As primeiras discussões ocorreram em 2006, e a web3 começou a aparecer em blogs e eventos de tecnologia. Em novembro daquele ano, o jornalista americano John Markoff mencionou a nova fase da internet na matéria “Uma Web guiada pelo bom senso?”, publicada no jornal norte-americano The New York Times. Ele disse o seguinte:

“Cientistas da computação e uma coleção crescente de empresas iniciantes estão encontrando novas maneiras de explorar a inteligência humana… Seu objetivo é adicionar uma camada de significado em cima da web existente que a tornaria menos um catálogo e mais um guia… Referido como Web 3.0, o esforço está em sua infância, e a própria ideia deu origem a céticos que a chamaram de uma visão inalcançável”.

Talvez naquela época ainda fosse quase inconcebível criar uma Internet diferente, como os céticos disseram para Markoff. No entanto, com o surgimento e a evolução de novas tecnologias, o cenário mudou. Em 2014, o cientista da computação Gavin Wood, cofundador do Ethereum (ETH) e um dos criadores da Polkadot (DOT), deu sua contribuição para o desenho do novo capítulo da rede mundial de computadores.

“A Web 3.0″, disse ele, “é uma reimaginação dos tipos de coisas para as quais já usamos na web, mas com um modelo fundamentalmente diferente para as interações entre as partes. Informações que assumimos como públicas, nós publicamos. Informações que supomos serem acordadas, colocamos em um livro-razão distribuído (sistema descentralizado de compartilhamento de dados). Informações que assumimos serem privadas, mantemos em segredo e nunca revelamos.”

O que muda em relação à Web 2.0?
Para sabermos exatamente o que muda na Web 3.0, é preciso olhar para as outras eras da Internet.

Web 1.0
A Web 1.0 começou no final da década de 80 e foi até 2000. Um dos principais marcos da época foi a criação do World Wide Web (WWW), sistema de documentos que dá aos usuários acesso a conteúdo multimídia. O criador foi o físico e cientista da computação Tim Berners-Lee.

Nessa fase, as páginas eram estáticas, e tinham muito texto e poucas imagens. A maioria dos sites pertenciam a veículos de imprensa, e a internet parecia mais com a TV e o Rádio. De fato, os usuários eram consumidores passivos e só conseguiam ler informações, sem interagir.
Grandes empresas de tecnologias foram criadas nessa época para “organizar” o conteúdo publicado, como Google e Yahoo.

Web 2.0
A partir dos anos 2000, a rigidez da Web 1.0 começou a dar espaço para uma Internet mais interativa – a Web 2.0. Empresas de tecnologia lançaram as primeiras plataformas para conversa e publicação de conteúdo. Aplicativos de bate-papo, como MSN e mIRC, blogs e redes sociais se popularizaram. Orkut, Facebook, Twitter e YouTube nasceram nessa época.

A Web 2.0, que dura até hoje, levou bilhões de usuários para dentro da Internet. Por outro lado, também marcou a monopolização da rede mundial de computadores. Os principais serviços, como buscadores e plataformas de mídias sociais, ficaram nas mãos dos grandes conglomerados de tecnologia. Os dados dos próprios usuários viraram moeda, às vezes sem eles saberem. Em outras palavras, a web ficou centralizada, à mercê da caneta dos CEOs.

Web 3.0
A Web 3.0 chegou com a pretensão de descentralizar a internet. A ideia é unir o que tem de melhor na Web 1.0 e 2.0, e tirar o controle da rede – e dos dados dos usuários – das mãos das big techs. Essa nova era digital está sendo construída aos poucos com ajuda de tecnologias inovadoras, principalmente a blockchain e as criptomoedas, que dispensam os validadores tradicionais de confiança (empresas, governos etc).

Qual a relação de Web 3.0 e criptoativos?
A Web 3.0 tem tudo a ver com os criptoativos por causa da blockchain, tecnologia subjacente que dá suporte para as moedas digitais. É essa tecnologia, cujo primeiro caso de uso foi o Bitcoin (BTC) no final de 2008, que está dando o caráter descentralizado da Internet do futuro.

A blockchain é um grande banco de dados compartilhado que registra as transações dos usuários. Para visualizá-la, pense nela como um sistema operacional rodando em diversos computadores espalhados pelo mundo. Todos os participantes (chamados de “nós”) podem ver e inserir dados, desde que sigam algumas regras pré-estabelecidas.

A diferença com um programa tradicional é que a blockchain, em seu formato público, não é controlada por uma entidade. Além disso, seu sistema é imutável – ou seja, a partir do momento que uma informação é registrada, não dá para alterá-la. Isso é possível por causa da forma como seu código foi criado, e de seus algoritmos.

Aplicativos descentralizadas (dApps), finanças descentralizadas (DeFi), tokens não-fungíveis (NFTs), metaverso e criptomoedas rodam nesse novo sistema.

“A Web 3.0 se trata da descentralização da internet como conhecemos, movendo de um contexto monopolizado por grandes instituições para outro no qual a rede é construída, operada e possuída pelos seus usuários. Para tornar essa descentralização possível, é necessário abraçar uma nova infraestrutura tecnológica, que nesse caso é a blockchain”, disse Bruno Diniz, diretor da Financial Data & Technology Association (FData) e sócio da Spiralem Innovation Consulting.

"""
texto2 = """
O Python tem chamado a atenção dos profissionais de TI nos últimos anos. Tanto é que um índice que mede a frequência de pesquisas na internet (Tiobe), aponta a linguagem de programação como a terceira mais procurada na web.

Pensando nisso, preparamos um conteúdo que destaca os principais usos do Python além de alguns caminhos de carreira que quem programa nessa linguagem pode ingressar.

O que é e para que serve o Python?
Gratuito e de código aberto, o Python foi lançado em 1991. Atualmente, possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation.

A linguagem, que pode ser utilizada para diversos fins, funciona emitindo comandos intuitivos, como, por exemplo, “print” para imprimir um texto na tela, “open” para abrir um arquivo, ou “find” para encontrar uma palavra.

Um dos usos do Python é automatizar tarefas, no entanto, a linguagem também permite coletar, organizar e salvar informações de páginas na internet; monitorar redes sociais; construir um site ou app; criar jogos; rodar algoritmos de machine learning; criar aplicações de inteligência artificial (IA), dentre outros.

Empregos para quem estuda Python
O conhecimento em Python pode ser um diferencial, e há uma série de planos de carreira disponíveis no mercado.

Esteja você apenas começando ou precisando de uma mudança na carreira, listamos abaixo cinco exemplos de trabalhos que devem ser considerados.

Analista GIS
Suas funções principais incluem: analisar dados espaciais por meio de software de mapeamento e projetar mapas digitais com dados geográficos.

Onde entra o Python? Pois bem, os scripts em Python permitem que os analistas GIS otimizem, por exemplo, o gerenciamento de dados.

Desenvolvedor de software
A função de um desenvolvedor envolve identificar, projetar, instalar e testar um sistema de software. Pode variar desde a criação de programas até a produção de sistemas que podem ser vendidos no mercado.

O Python é uma linguagem comum que pode ser usada no processo de desenvolvimento, ou seja, o conhecimento da linguagem pode ser a chave para conseguir um emprego como desenvolvedor.

Engenheiro de Qualidade
Um engenheiro de QA é responsável pela criação de testes para identificar problemas em softwares. Eles identificam e analisam quaisquer bugs e erros encontrados durante a fase de teste e os documentam para revisão posterior.

Outras tarefas incluem: desenvolver e executar novos testes, relatar os resultados e colaborar com desenvolvedores de software para corrigir problemas.

Proficiência em Python também é importante para uma função que envolve controle de qualidade.

Desenvolvedor Full Stack
Os desenvolvedores Full Stack precisam ter algumas habilidades em nichos como: codificação, bancos de dados e design gráfico para fazer o seu trabalho.

Eles são uma espécie de “pau para toda obra”. A descrição do trabalho geralmente inclui o uso de uma variedade de tecnologias e linguagens para desenvolver aplicativos.

Engenheiro de Aprendizado de Máquina
Um engenheiro de aprendizado de máquina é a pessoa em TI que se concentra em pesquisar, construir e projetar sistemas de inteligência artificial para automatização. Esses engenheiros projetam e criam algoritmos de IA capazes de aprender e fazer previsões.

No fim, essas são apenas alguns exemplos do que você pode fazer com conhecimento em Python. Existem várias outras opções por aí e novos aplicativos saindo do forno diariamente graças ao Phyton.
"""

# contando as letras minúsculas:
aparicoes_texto1 = Counter(texto1.lower())
print(aparicoes_texto1)
print("-----------------------------------------------------------------------------------------------------")
# contando as palvras:
print(Counter(texto1.split()))
print("-----------------------------------------------------------------------------------------------------")

#número de caractéres presente no texto 1:
total_caracteres_texto1 = sum(aparicoes_texto1.values())
print(total_caracteres_texto1)
print("-----------------------------------------------------------------------------------------------------")

# frequência de apararições de letras em porcentagem:
for letra, frequencia in aparicoes_texto1.items():
    tupla = letra, frequencia / total_caracteres_texto1 *100
    print(tupla)
print("-----------------------------------------------------------------------------------------------------")

# passando o laço para list comprehension em list comprehension
proporcoes = [(letra, frequencia / total_caracteres_texto1 * 100) for letra, frequencia in aparicoes_texto1.items()]
print(proporcoes)

#relembrando: o Counter por padrão, organiza do mais frenquente ao menos frequente.
proporcoes = Counter(dict(proporcoes))
print(proporcoes)

print(proporcoes.most_common(10)) #most_commom provém do Counter.

#criando uma função abaixo, utilizando a lógica acima:
def analise_frequencia_de_letras(texto):
    aparicoes_texto = Counter(texto.lower())
    total_caracteres_texto = sum(aparicoes_texto.values())
    proporcoes = [(letra, frequencia / total_caracteres_texto) for letra, frequencia in aparicoes_texto.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:2f}%".format(caractere, proporcao*100))
analise_frequencia_de_letras(texto1)
print("-----------------------------------------------------------------------------------------------------")
analise_frequencia_de_letras(texto2)