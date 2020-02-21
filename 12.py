import datetime
from datetime import time,datetime
year = raw_input('Dwse xronia ')
month= raw_input('Dwse mina ')
day= raw_input ('Dwse mera ')
year1=int(year)
datt= year+'-'+month+'-'+day
d= datetime.strptime(datt, "%Y-%m-%d")
def date_diff_in_seconds(dat2, dat1):
  timedelta = abs(dat2 - dat1)
  return timedelta.days * 24 * 3600 + timedelta.seconds
def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)
date1 = d
date2 = datetime.now()
print("xronos pou apexei h trexousa apo thn dothisa hmerominia\n%d meres, %d wres, %d lepta, %d defterolpeta" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))
if month=='1' or month=='01':
 print ("o minas exei 31 meres")
elif month=='2' or month=='02':
 if(year1%4==0 and year1%100!=0 or year1%400==0):
         print ("o minas exei 29 meres")
 else:
         print ("o minas exei 28 meres")
elif month=='3' or month=='03':
 print ("o minas exei 31 meres")
elif month=='4' or month=='04':
 print ("o minas exei 30 meres")
elif month=='5' or month=='05':
 print ("o minas exei 31 meres")
elif month=='6' or month=='06':
 print ("o minas exei 30 meres")
elif month=='7' or month=='07':
 print ("o minas exei 31 meres")
elif month=='8' or month=='08':
 print ("o minas exei 31 meres")
elif month=='9' or month=='09':
 print ("o minas exei 30 meres")
elif month=='10' or month=='10':
 print ("o minas exei 31 meres")
elif month=='11' or month=='11':
 print ("o minas exei 30 meres")
elif month=='12' or month=='12':
 print ("o minas exei 31 meres")
        
        
        
 
