with open('5.txt','r') as f:
    for line in f:
        for word in line.split():
           a= len (word)
           if a > 3 :
            word= word [:0] + word [1:] + word [:1]+"ay"
            print (word) 
           elif a< 3 :
              print (word)
            
