def test_number(number):

    a = 0 
    b = number % 2

    if b == 0 :
        a = print("Par")
    else:
        a = print("Impar")
    return a 

resp = int(input('Digite um numero: '))
test_number(resp)