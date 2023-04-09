import math
def prime(n):
  if(n==1):
    return False
  result=True
  for i in range(2,int(math.sqrt(n)+1)):
    if(n%i==0):
      result=False
      break
  return result


def prime_diff(m):
  pd={}
  prev=2
  for i in range(3,m+1):
    d=i-prev
    prev=i
    if d in pd.keys():
      pd[d]+=1
    else:
      pd[d]=1
  return pd
