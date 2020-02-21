x=input("dwse mia leksh: ")
asc=""
for i in x:
    asc=asc+str(ord(i))
print(asc)
i=0
for j in range(1,int(asc)+1):
    if int(asc)%j==0:
        i=i+1
if i==2:
    print("o arithmos einai prwtos")
else:
    print("o arithmos den einai prwtos")
