import random
fanari1= random.randint(0, 15)
fanari2= random.randint(0, 15)
fanari3= random.randint(0, 15)
fanarialist1=['fanari1','fanari2']
fanarialist2=['fanari1','fanari3']
fanarialist3=['fanari3','fanari2']
fanarialsit4=['fanari1','fanari2','fanari3']

while fanari1+fanari2+fanari3!=0:
 if max(fanari1,fanari2,fanari3)==fanari1 :
    autokinhtagone=random.randint(5,10)
    autokinhtacome2=random.randint(0,5)
    autokinhtacome3=random.randint(0,5)
    print ('green fanari1','red fanari2 kai fanari3') 
    print ('prin to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3)
    fanari2=fanari2+autokinhtacome2
    fanari3=fanari3+autokinhtacome3
    if fanari1>=autokinhtagone:
     fanari1=fanari1-autokinhtagone
     print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari1',autokinhtagone,'autokinhta','sto fanari2 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
    else:
     fanari1=0
     print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari1',fanari1,'autokinhta','sto fanari2 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
 elif max(fanari1,fanari2,fanari3)==fanari2:
     autokinhtagone=random.randint(5,10)
     autokinhtacome2=random.randint(0,5)
     autokinhtacome3=random.randint(0,5)
     print ('green fanari2','red fanari1 kai fanari3')
     print ('prin to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3)
     fanari1=fanari1+autokinhtacome2
     fanari3=fanari1+autokinhtacome3
     if fanari2>=autokinhtagone:
      fanari2=fanari2-autokinhtagone
      print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari2',autokinhtagone,'autokinhta','sto fanari1 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
     else:
      fanari2=0
      print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari2',fanari2,'autokinhta','sto fanari1 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
 elif max(fanari1,fanari2,fanari3)==fanari3:
     autokinhtagone=random.randint(5,10)
     autokinhtacome2=random.randint(0,5)
     autokinhtacome3=random.randint(0,5)
     print ('green fanari3','red fanari2 kai fanari1')
     print ('prin to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3)
     fanari1=fanari1+autokinhtacome2
     fanari2=fanari2+autokinhtacome3
     if fanari3>=autokinhtagone:
         fanari3=fanari3-autokinhtagone
         print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari3',autokinhtagone,'autokinhta','sto fanari2 hrthan',autokinhtacome3,'autokinhta','kai sto fanari1 hrthan',autokinhtacome2,'autokinhta')
     else:
         fanari3=0
         print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari3',fanari3,'autokinhta','sto fanari2 hrthan',autokinhtacome3,'autokinhta','kai sto fanari1 hrthan',autokinhtacome2,'autokinhta')
 elif max(fanari1,fanari2,fanari3)==fanari1 and max(fanari1,fanari2,fanari3)==fanari2:
    maxfanari=random.choice(fanarialist1)
    if maxfanari=='fanari1':
     autokinhtagone=random.randint(5,10)
     autokinhtacome2=random.randint(0,5)
     autokinhtacome3=random.randint(0,5)
     print ('green fanari1','red fanari2 kai fanari3') 
     print ('prin to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3)
     fanari2=fanari2+autokinhtacome2
     fanari3=fanari3+autokinhtacome3
     if fanari1>=autokinhtagone:
      fanari1=fanari1-autokinhtagone
      print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari1',autokinhtagone,'autokinhta','sto fanari2 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
     else:
      fanari1=0
      print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari1',fanari1,'autokinhta','sto fanari2 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
    else:
      autokinhtagone=random.randint(5,10)
      autokinhtacome2=random.randint(0,5)
      autokinhtacome3=random.randint(0,5)
      print ('green fanari2','red fanari1 kai fanari3')
      print ('prin to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3)
      fanari1=fanari1+autokinhtacome2
      fanari3=fanari1+autokinhtacome3
      if fanari2>=autokinhtagone:
       fanari2=fanari2-autokinhtagone
       print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari2',autokinhtagone,'autokinhta','sto fanari1 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
      else:
       fanari2=0
       print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari2',fanari2,'autokinhta','sto fanari1 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
 elif max(fanari1,fanari2,fanari3)==fanari1 and max(fanari1,fanari2,fanari3)==fanari3:
     maxfanari2=random.choice(fanarialist2)
     if maxfanari2=='fanari1':
       autokinhtagone=random.randint(5,10)
       autokinhtacome2=random.randint(0,5)
       autokinhtacome3=random.randint(0,5)
       print ('green fanari1','red fanari2 kai fanari3') 
       print ('prin to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3)
       fanari2=fanari2+autokinhtacome2
       fanari3=fanari3+autokinhtacome3
       if fanari1>=autokinhtagone:
        fanari1=fanari1-autokinhtagone
        print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari1',autokinhtagone,'autokinhta','sto fanari2 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
       else:
        fanari1=0
        print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari1',fanari1,'autokinhta','sto fanari2 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
     else:
      autokinhtagone=random.randint(5,10)
      autokinhtacome2=random.randint(0,5)
      autokinhtacome3=random.randint(0,5)
      print ('green fanari3','red fanari2 kai fanari1')
      print ('prin to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3)
      fanari1=fanari1+autokinhtacome2
      fanari2=fanari2+autokinhtacome3
      if fanari3>=autokinhtagone:
         fanari3=fanari3-autokinhtagone
         print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari3',autokinhtagone,'autokinhta','sto fanari2 hrthan',autokinhtacome3,'autokinhta','kai sto fanari1 hrthan',autokinhtacome2,'autokinhta')
      else:
         fanari3=0
         print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari3',fanari3,'autokinhta','sto fanari2 hrthan',autokinhtacome3,'autokinhta','kai sto fanari1 hrthan',autokinhtacome2,'autokinhta')
 elif max(fanari1,fanari2,fanari3)==fanari2 and max(fanari1,fanari2,fanari3)==fanari3:
    maxfanari3=random.choice(fanarialist3)
    if maxfanari3=='fanari2':
     autokinhtagone=random.randint(5,10)
     autokinhtacome2=random.randint(0,5)
     autokinhtacome3=random.randint(0,5)
     print ('green fanari2','red fanari1 kai fanari3')
     print ('prin to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3)
     fanari1=fanari1+autokinhtacome2
     fanari3=fanari1+autokinhtacome3
     if fanari2>=autokinhtagone:
      fanari2=fanari2-autokinhtagone
      print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari2',autokinhtagone,'autokinhta','sto fanari1 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
     else:
       fanari2=0
       print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari2',fanari2,'autokinhta','sto fanari1 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
    else:
     autokinhtagone=random.randint(5,10)
     autokinhtacome2=random.randint(0,5)
     autokinhtacome3=random.randint(0,5)
     print ('green fanari3','red fanari2 kai fanari1')
     print ('prin to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3)
     fanari1=fanari1+autokinhtacome2
     fanari2=fanari2+autokinhtacome3
     if fanari3>=autokinhtagone:
         fanari3=fanari3-autokinhtagone
         print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari3',autokinhtagone,'autokinhta','sto fanari2 hrthan',autokinhtacome3,'autokinhta','kai sto fanari1 hrthan',autokinhtacome2,'autokinhta')
     else:
         fanari3=0
         print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari3',fanari3,'autokinhta','sto fanari2 hrthan',autokinhtacome3,'autokinhta','kai sto fanari1 hrthan',autokinhtacome2,'autokinhta')
 elif max(fanari1,fanari2,fanari3)==fanari2 and max(fanari1,fanari2,fanari3)==fanari3 and max(fanari1,fanari2,fanari3)==fanari1:
    maxfanari4= random.choice(fanarialist4)
    if maxfanari4== 'fanari1' :
      autokinhtagone=random.randint(5,10)
      autokinhtacome2=random.randint(0,5)
      autokinhtacome3=random.randint(0,5)
      print ('green fanari1','red fanari2 kai fanari3') 
      print ('prin to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3)
      fanari2=fanari2+autokinhtacome2
      fanari3=fanari3+autokinhtacome3
      if fanari1>=autokinhtagone:
        fanari1=fanari1-autokinhtagone
        print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari1',autokinhtagone,'autokinhta','sto fanari2 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
      else:
        fanari1=0
        print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari1',fanari1,'autokinhta','sto fanari2 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
    elif maxfanari4== 'fanari2':
     autokinhtagone=random.randint(5,10)
     autokinhtacome2=random.randint(0,5)
     autokinhtacome3=random.randint(0,5)
     print ('green fanari2','red fanari1 kai fanari3')
     print ('prin to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3)
     fanari1=fanari1+autokinhtacome2
     fanari3=fanari1+autokinhtacome3
     if fanari2>=autokinhtagone:
      fanari2=fanari2-autokinhtagone
      print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari2',autokinhtagone,'autokinhta','sto fanari1 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
     else:
       fanari2=0
       print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari2',fanari2,'autokinhta','sto fanari1 hrthan',autokinhtacome2,'autokinhta','kai sto fanari3 hrthan',autokinhtacome3,'autokinhta')
    else:
     autokinhtagone=random.randint(5,10)
     autokinhtacome2=random.randint(0,5)
     autokinhtacome3=random.randint(0,5)
     print ('green fanari3','red fanari2 kai fanari1')
     print ('prin to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3)
     fanari1=fanari1+autokinhtacome2
     fanari2=fanari2+autokinhtacome3
     if fanari3>=autokinhtagone:
         fanari3=fanari3-autokinhtagone
         print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari3',autokinhtagone,'autokinhta','sto fanari2 hrthan',autokinhtacome3,'autokinhta','kai sto fanari1 hrthan',autokinhtacome2,'autokinhta')
     else:
         fanari3=0
         print ('meta to anama fanari1:',fanari1,'fanari2',fanari2,'fanari3',fanari3,'efugan apo to fanari3',fanari3,'autokinhta','sto fanari2 hrthan',autokinhtacome3,'autokinhta','kai sto fanari1 hrthan',autokinhtacome2,'autokinhta')

