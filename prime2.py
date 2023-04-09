'''Checking primality method 2'''

import math 
result=True

def prime(m):
  for i in range(2,int(math.sqrt(m)+1):
           if(m%i==0):
                 result=False
                 break
  return result
                 
