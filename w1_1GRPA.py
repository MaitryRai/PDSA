'''find min difference subset of size P from a list L'''

def min_difference(L,p):
  L.sort
  l=len(L)
  min=L[p-1]-L[0]
  for i in range(0,l-p+1):
    if(min<L[p-1+i]-L[i]):
      min=L[p-1+i]-L[i]
  return min
