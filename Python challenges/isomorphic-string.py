def is_isomorphic(str1, str2):
    """
    Insira duas strings e o programa irá checar se ela são isomórficas
    """
    if len(str1) != len(str2):
        return False
    
    list1 = []
    list2 = []

    for i in str1:
        if i in list1:
            continue
        
        list1.append(i)
    
    for i in str2:
        if i in list2:
            continue
        
        list2.append(i)
    

    if len(list1) != len(list2):
        return False
    
    map = {}

    for i in range(0, len(list1)):
        map[list1[i]] = list2[i]
    
    
    test_str1 = str1
    test_str2 = str2

    for key, value in map.items():
        test_str1.replace(key, value )
        test_str2.replace(value, key)

    if test_str1 == str1 and test_str2 == str2:
        return True
    else:
        return False


print(is_isomorphic('bolo', 'sala'))