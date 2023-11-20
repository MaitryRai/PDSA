GRPA3 WEEK1:
def odd_one(L):
  P={}
  for ele in L:
    a=type(ele)
    if(a in P.keys()):
      P[a]=P[a]+1
    else:
      P[a]=1

  for k in P.keys():
    if(P[k]==1):
      return k 


L=[1,2,3,4,True]
print(odd_one(L))
    
