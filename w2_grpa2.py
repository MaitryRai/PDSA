'''Goldbach Conjecture'''

import math
def prime(n):
  result=True
  for i in range(2,int(math.sqrt(n))+1):
    if(n%i==0):
      result=False
      break
  return result

def goldbach_conjecture(n):
  gl=[]
  for i in range(2,n//2+1):
    if(prime(i)):
      if(prime(n-i)):
        gl.append((i,n-i))
  return gl

print(goldbach_conjecture(30))
