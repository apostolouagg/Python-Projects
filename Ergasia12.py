from datetime import datetime
currenttime = datetime.now()
date_format = "%d-%m-%Y %H:%M:%S"
time1 = str(input("dwse hmeromhnia se morfh mera-mhnas-xronia(01-01-2000): "))
try:
    time2 = datetime.strptime(time1+" 00:00:00", date_format)
    if currenttime>time2:
        diff = currenttime - time2
    else:
        diff = time2 - currenttime
    a=(str(diff).split())
    b=(a[2].split(":"))
    print ("Apexei" ,a[0], "days,", b[0], "hours,", b[2], "seconds")
    meres=[0,0,0,0,0,0,0,0,0,0,0,0]
    flag=False
    time3 = time1.split("-")
    if (int(time3[2]) % 4) == 0:
       if (int(time3[2]) % 100) == 0:
           if (int(time3[2]) % 400) == 0:
               flag=True
           else:
               flag=False
       else:
           flag=True
    else:
        flag=False
    if flag==True:
        for i in range(7):
            if i%2==0:
                meres[i]=31
            else:
                if i==1:
                    meres[i]=29
                else:
                    meres[i]=30
        for i in range(7,12):
            if i%2!=0:
                meres[i]=31
            else:
                meres[i]=30
    else:
        for i in range(7):
            if i%2==0:
                meres[i]=31
            else:
                if i==1:
                    meres[i]=28
                else:
                    meres[i]=30
        for i in range(7,12):
            if i%2!=0:
                meres[i]=31
            else:
                meres[i]=30
    print ("O mhnas ayths ths hmeromhnias exei:", meres[int(time3[1])],"meres")
        
except:
    print("kati kaneis lathos sthn hmeromhnia mastora")
    print("auth einai h swsth morfh: mera-mhnas-xronia(01-01-2000)")
    raise Exception()
