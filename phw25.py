def break_words(stuff):
    """Esta função irá dividir palavras para nós."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Ordenar palavras"""
    return sorted(words)

def print_first_word(words):
    """imprime a primeira palavra depois de tirá-la do conjunto."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Imprime a última palavra depois de tirá-la do conjunto"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Recebe uma frase completa e retorna as palavras ordenadas."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Imprime a primeira e a última palavra de uma frase."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Ordena as palavras e imprime a primeira e a última."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

sentence = "Esta função irá dividir palavras para nós."
print_first_and_last(sentence)