from tkinter import *
from tkinter.messagebox import *

def show_answer():
    da,ma,ya= [int(da) for da in date1.get().split('/')]
    db,mb,yb= [int(db) for db in date2.get().split('/')]
    
    if(yb>ya or (ya==yb & mb>ma) or (ya==yb & ma==mb & db>da)):
        y1=ya
        y2=yb
        m1=ma
        m2=mb
        d1=da
        d2=db
    else:
        y1=yb
        y2=ya
        m1=mb
        m2=ma
        d1=db
        d2=da
    if(y1!=y2 or y1==y2 & m1!=m1):
        if(m1==1 or m1==3 or m1==5 or m1==7 or m1==8 or m1==10 or m1==12 ) :
            days=(31-d1)+d2
        elif(m1==4 or m1==6 or m1==9 or m1==11) :
            days=(30-d1)+d2
        else:
            if((y1%4==0 & y1%100==0 & y1%400) or (y1%4==0 & y1%100!=0)):
                days=(29-d1)+d2
            else:
                days=(28-d1)+d2
    else:
        days=d2-d1+1
    if(y1!=y2):
        for m in range(m1+1,13):
            if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12 ) :
                days=(days+31)
            elif(m==4 or m==6 or m==9 or m==11) :
                days=(days+30)
            else:
                if((y1%4==0 & y1%100==0 & y1%400) or (y1%4==0 & y1%100!=0)):
                    days=(days+29)
                else:
                    days=(days+ 28)
        for mf in range(1,m2):
            if(mf==1 or mf==3 or mf==5 or mf==7 or mf==8 or mf==10 or mf==12 ) :
                days=(days+31)
            elif(mf==4 or mf==6 or mf==9 or mf==11) :
                days=(days+30)
            else:
                if((y1%4==0 & y1%100==0 & y1%400) or (y1%4==0 & y1%100!=0)):
                    days=(days+29)
                else:
                    days=(days+ 28)
        for y in range(y1+1,y2):
            if((y1%4==0 & y1%100==0 & y1%400) or (y1%4==0 & y1%100!=0)):
                days=days+366 +1/4
            else:
                days=days+365+1/4
    else:
        for m in range(m1+1,m2):
            if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12 ) :
                days=(days+31)
            elif(m==4 or m==6 or m==9 or m==11) :
                days=(days+30)
            else:
                if((y1%4==0 & y1%100==0 & y1%400) or (y1%4==0 & y1%100!=0)):
                    days=(days+29)
                else:
                    days=(days+ 28)
    ans=str(round(days))
    Label(main, text = ans+':Days').grid(row=3)


main = Tk()
Label(main, text = "").grid(row=0)
Label(main, text = "Enter 1st Date:").grid(row=1)
Label(main, text = "Enter 2nd Date:").grid(row=2)
main.title('Days Calculation')
Label(main, text = "Thank you! @Sayikumarr").grid(row=6)


date1 = Entry(main)
date1.insert(0, 'DD/MM/YYYY')
date2 = Entry(main)
date2.insert(0, 'DD/MM/YYYY')


date1.grid(row=1, column=1)
date2.grid(row=2, column=1)



Button(main, text='Quit', command=main.quit).grid(row=5, column=0)
Button(main, text='Show', command=show_answer).grid(row=5, column=1)

mainloop()