txt=open("apostolou.txt")
x=txt.read()
y=x.split()
for w in y:
    i=0
    j=0
    for char in w:
        if(char=="f" or char=="c" or char=="k" or char=="r"):
            i=i+1
        else:
            j=j+1
    if(i>j):
        print("h leksh einai kakh")
        i=0
        j=0
    else:
        print("h leksh einai kalh")
        j=0
        i=0
