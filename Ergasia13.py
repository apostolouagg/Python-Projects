x=str(input("dwse enan 16pshfio arithmo: "))
sum=0
for i in range(16):
  if i%2==0:
    y=int(x[i])*2
    if y>9:
      numstr=str(y)
      for j in range(len(numstr)):
          sum=sum+int(numstr[j])
    else:
      sum=sum+y
  else:
    sum=sum+int(x[i])
if sum%10==0:
  print("h karta einai egkurh")
else:
  print("h karta den einai egkurh")
