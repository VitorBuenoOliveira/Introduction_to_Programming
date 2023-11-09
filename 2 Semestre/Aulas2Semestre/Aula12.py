def fatorial(n:int):
    if n==1:
        return n
    else:
        return n * fatorial(n-1)
    
def contagem_regressiva(n:int):
    print(n)
    if(n>0):
        contagem_regressiva(n-1)

#3! = 3.2.1 =6
#5! = 5.4.3.2.1=120

#15 = 1111

def binario(n:int)-> str:
    if n < 2:
        return n
    else:
        quociente = binario(n//2)
        resto = n%2
        return f'{quociente}{resto}'
    

r = binario(15)

print(f'{r}')
   

   
