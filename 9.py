def athroisma( number): 
    sum = 0
    number= number*3+1
    while(number > 0 or len(str(sum)) > 1): 
        if(number == 0): 
            number = sum
            sum = 0
            number= number*3+1
        sum += number % 10
        number /= 10
    return sum
number = input("Dwse airthmo: ")
print (athroisma(number))
  
