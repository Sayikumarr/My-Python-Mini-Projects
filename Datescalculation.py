d1,m1,y1= [int(d1) for d1 in input("Enter 1st date as DD/MM/YYYY: ").split('/')]
d2,m2,y2= [int(d2) for d2 in input("Enter 2nd date as DD/MM/YYYY: ").split('/')]
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
print(round(days),'-Days')