# Índice Invertido

## Descrição

1. Implementação de um gerador de índice invertido;
2. Implementação do modelo booleano para recuperação de informação.

## A entrada do programa
O programa recebe dois argumentos como entrada pela linha de comando. O primeiro argumento especifica o caminho de um arquivo texto que contém os caminhos de todos os arquivos que
compõem a base, cada um em uma linha. O segundo argumento especifica o caminho de um arquivo texto que traz uma consulta a ser respondida.

## A saída do programa
O programa irá gerar dois arquivo de saída, com nomes e conteúdo exatamente como a seguir:
• indice.txt : arquivo que contem o índice invertido gerado a partir dos documentos da base.
• resposta.txt : arquivo com os nomes dos documentos que atendem a consulta do usuário segundo o modelo booleano.

## Arquivo indice.txt:
O programa irá gerar um arquivo chamado indice.txt, que contem o índice invertido gerado a partir dos documentos da base. Para cada um dos termos no índice, é preciso apontar o número do arquivo em que o mesmo aparece, e a quantidade de vezes em que o mesmo aparece no arquivo. Os arquivos são numerados segundo a ordem em que aparecem no arquivo que indica os documentos, no caso, base.txt. Assim, o arquivo a.txt é o arquivo 1, o arquivo b.txt é o arquivo 2 e, por
fim, o arquivo c.txt é o arquivo 3.

## Arquivo resposta.txt
O arquivo resposta.txt contém a resposta à consulta contida no arquivo de consulta, no caso, consulta.txt. A primeira linha desse arquivo deve conter a quantidade de documentos que satisfazem a consulta. As demais linhas contém os arquivos da base que atendem a consulta, um por linha, conforme o exemplo a seguir, onde respondemos a consulta especificada em nosso arquivo consulta.txt. Será preciso considerar todas as disjunções da consulta, além de desconsiderar stopwords presentes na mesma e também lematizar seus termos.

# Como executar: 

### Passo 1:

`python modelo_booleano.py base.txt consulta.txt`

### Passo 2: 

`python3 waxm_corretor_modelo_booleano.pyc base.txt consulta.txt modelo_booleano.py`
<br>ou<br>
`py waxm_corretor_modelo_booleano.pyc base.txt consulta.txt modelo_booleano.py`