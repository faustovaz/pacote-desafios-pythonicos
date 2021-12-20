"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys

def count(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.rstrip().lower() for line in file.readlines()]
        words = " ".join(lines).split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return word_count

# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).
def print_words(filename):
    word_count = count(filename)
    top_words = list(word_count.items())
    top_words.sort(key=lambda i:i[0])
    for key,value in top_words:
        print(f'{key} {value}')

# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def print_top(filename):
    word_count = count(filename)
    top_words = list(word_count.items())
    top_words.sort(key=lambda i:i[-1], reverse=True)
    for key, value in top_words[:10]:
        print(f'{key} {value}')


def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
