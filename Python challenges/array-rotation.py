def rotation_array(n, k):
    """
    Função que entra um valor 'n' que indica uma lista que vai de 1 até esse valor, e o 'k' que 
    indica quantos valores do final da lista serão pegos. Assim, ele pega esses valores finais
    e joga para o inicio da lista.
    """
    list = []
    for i in range(1, n + 1):
        list.append(i)
    
    last_values = []

    for i in range(0, k):
        last_values.append(n - i)
    
    for i in last_values:
        list.remove(i)
        list.insert(0, i)

    return list

list = int(input('Insira o tamanho da lista: '))
last = int(input('Insira os ultimos valores para fazer a rotação: '))

print(rotation_array(list, last))