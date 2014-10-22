def duplikaty(lista):
    dupli=[]
    for i in lista:
        if i not in dupli:
            dupli.append(i)
    return dupli

lista=['a', 'b', 'c', 'a']
print duplikaty(lista)
