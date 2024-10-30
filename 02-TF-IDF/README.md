# TF IDF

## Descrição
Este trabalho consiste na da ponderação TF-IDF (com logaritmo na base 10).

`TF−IDFij=(1+log f ij)log(N/ni),se fij>0`

`TF−IDFij=0,se fij=0`

## A entrada do programa
O programa recebe um argumento de entrada pela linha de comando. O primeiro argumento
especifica o caminho de um arquivo texto que contém os caminhos de todos os arquivos que compõem a base, cada um em uma linha.

## A saída do programa
O programa gera dois arquivos de saída, com nomes e conteúdo exatamente como a seguir:
• indice.txt: arquivo que contem o índice invertido gerado a partir dos documentos da base.
• pesos.txt: arquivo que contém a ponderação TF-IDF de cada documento.

## Arquivo pesos.txt
O programa irá gerar um arquivo texto chamado pesos.txt que contém os pesos de cada termo em cada documento segundo a ponderação TF-IDF (com cálculo de logaritmo na base 10). Cada linha desse arquivo deve conter os pesos não nulos dos termos de um dos documentos da base.

# Como executar: 

### Passo 1:

`python tfidf.py base.txt`

### Passo 2: 

`python3 waxm_corretor_tfidf.pyc base.txt tfidf.py`
<br>ou<br>
`py waxm_corretor_tfidf.pyc base.txt tfidf.py`