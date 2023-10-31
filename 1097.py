a=input ()
s='';l=0
for i in a:
  l+=1
  if int(i)!=9:
    s+=str('9')+str(a[l:])
    break
  else:
    s+=str ('9')
print (s)
