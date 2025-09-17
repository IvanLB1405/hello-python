def word_counter(text, word):
    return text.lower().split().count(word.lower())

#Pasamos texto a minus, lo partimos con split(sin argumentos, por defecto es el whitespace) y contamos el substring word
#en minusculas tambien