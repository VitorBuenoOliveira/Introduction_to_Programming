def fatorial(n):
    if n <= 1:
        return n
    else:
        return n * fatorial(n-1)
    
import unittest

def teste_fatorial():
    assert fatorial(4) == 24

if __name__ == '__main__':
    teste_fatorial()