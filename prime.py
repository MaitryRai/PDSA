def prime(m):
  result=false
  for i in range(2,m//2+1):
    if(m%i==0):
      result=true
      break
  return result
      
