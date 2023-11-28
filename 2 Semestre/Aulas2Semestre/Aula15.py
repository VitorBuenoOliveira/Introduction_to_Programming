def canBeBigger(n):
    lista_n = []#Numero exemplo 9871
    while n>0:
        lista_n.append(n%10)
        n /= 10 #Saida tem que ser ex:[1,7,8,9]
        while len(lista_n)>0:
            f = lista_n.pop(0)
            for i in lista_n:
                if f < i :
                    return True
        return False


def next_bigger_bad(n:int) -> int:
    if not canBeBigger(n):
        return -1
    next = n+1
    while True:
        str_next = [i for i in str(next)]
        str_n = str(n)
        for s in str_n:
            if s in str_next:
                str_next.remove(s)


        if len(str_next)==0:
            return next
        else:
            next += 1

r = canBeBigger(9871)
c = next_bigger_bad(r)

print(f'{c}')