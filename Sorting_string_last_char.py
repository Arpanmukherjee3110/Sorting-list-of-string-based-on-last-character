#Given a list of strings, write a program to write sort the list of strings on the basis of last character of each string.
#Input: L = ['ram', 'shyam', 'lakshami']
#Output: ['lakshami', 'ram', 'shyam']


def fun(s):
  ln=len(s)
  asc=ord(s[ln-1])
  return asc
def func(s1,s2):
  ln=min(len(s1),len(s2))
  s=""
  while(ln>0):
    ln=ln-1
    m=ord(s1[ln])
    n=ord(s2[ln])
    if m<n:
      s=s1
      break
    if n<m:
      s=s2
      break
    if n==m:
      continue
  if len(s)==0 and len(s1)==len(s2):
    s=s1
  if len(s)==0 and len(s1)!=len(s2):
    if len(s1)>len(s2):
      s=s1
    if len(s1)<len(s2):
      s=s2
  return s
L=list(map(str,input().split()))
l=len(L)
K=[]
check=fun(L[0])
index=0
while(len(L)!=0):
  check=fun(L[0])
  index=0
  for i in range(len(L)):
    if fun(L[i])<check:
      check=fun(L[i])
      index=i
      continue
    if fun(L[i])==check:
      ss=func(L[index],L[i])
      if ss==L[i]:
        index=i
  K.append(L[index])
  L.remove(L[index])
  l=len(L)
  
print(K)