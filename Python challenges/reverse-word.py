def reverse_string(string):
    """
    Insira uma string como uma frase, e a função irá retornar essa string com a frase invertida.
    """
    string_list = (string.split(' '))[::-1]
    reversed_string = ' '.join(string_list)
    return reversed_string

string = input('Insira uma frase para ser invertida: ')
print(reverse_string(string))
