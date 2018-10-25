#Simple Cipher Algorithm
from random import shuffle
from random import randrange

def cipher(s):
   key = [chr(i+65) for i in range(26)]
   shuffle(key)
   out = ""
   for c in s:
       ascii = ord(c)
       if ascii > 64 and ascii < 91:
           out += key[ascii-65]
       else:
           out += c
   return out

print(cipher("BONNE NUIT LES PETITS"))


def kill2(t,k,u):
   out = t
   while not u in out:
       key = [randrange(1, 27) for i in range (k)]
       out,i = "",0
       for c in t:
           out += chr((ord(c)-65+key[i])%26+65)
           i = (i+1)%k
   return out
print(kill2("LBJNKVXSBURPRCIDPNYDXO", 4, "ESTBEAU"))

#### EXPLOSION ####

def fibonacci(n):
    (a,b) = (1,1) if n == 1 else fibonacci(n-1)
    return b, a+b
print(fibonacci(100)[0])

#### AND CERTAINLY NOT: ####
def fibonnacci(n):
    x = 1 if n <= 1 else fibonacci(n-1)+fibonacci(n-2)
    return x
print(fibonacci(100))





