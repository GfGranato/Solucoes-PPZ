print('=====1=====')
from random import randint
sorte =[]


for k in range (10):
     sorte.append(randint(1,100))

maior = menor = sorte[0]
k=0
while k<10:
     if menor < sorte[k]:
          menor = sorte[k]

     if maior > sorte[k]:
          maior = sorte[k]
     k+=1
print(f'sorte: {sorte}')
print(f'Menor: {menor}')
print(f'Maior: {maior}')

print('=====2=====')

from random import randint
sorte=[]
par=[]
impar=[]
for k in range (20):
     sorte.append(randint(1,100))
k=0
while k<20:
     if sorte[k] % 2==0:
          par.append(sorte[k])
     else:
          impar.append(sorte [k])
     k+=1
print(f'sorte: {sorte}')
print(f'par: {par}')
print(f'impar: {impar}')

print('======3======')


from random import randint
v1=[]
v2=[]
vf=[]

for k in range(10):
     v1.append(randint(1,100))
     v2.append(randint(1,100))

print(f':v1: {v1}')
print(f':v2: {v2}')
k=0
while k<10:
     vf.append(v1[k])
     vf.append(v2[k])
     k+=1
print(vf)

print('===4=e=5=====')

texto = '''The Python Software Foundation and the global
   Python community  welcome and encourage participation
   by everyone. Our community is based on mutual respect,
   tolerance, and encouragement, and we are working to
   help each other live up to these principles. We want
   our community to be more diverse: whoever you are, and
   whatever your background, we welcome you.'''.lower()
import string
j=0

lista=[]

def cont(palavra):
     for letra in palavra:
          if letra in 'python':
               return True
          
     return False

for c in string.punctuation:
  texto = texto.replace(c, ' ')
r4=[]
for p in texto.split():
     if p in texto.split():
          if cont(p) and len (p) >4:
               r4.append(p)

for k in texto.split():
     
     if k[0] in 'python' or k[-1] in 'python':
          lista.append(k)
          j=j+1
          

print(f'Nº total de palavras com "python": {j}')
print(f'Nº de palavras com uma das letras "python" e com mais de 4 letras: {len(r4)}')





