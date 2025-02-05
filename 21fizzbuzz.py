

for i in range(1, 101):
    if i%3 == 0 and i%5 == 0: print("Fizzbuzz");    #print("FizzBuzz", i)
    elif i%3 == 0:            print("Fizz");        #print("Fizz", i)
    elif i%5 == 0:            print("Buzz");        #print("Buzz", i) 
    else:                     print(i)

#must use if elif else, otherwise can get repeats of Fizzbuzz then Fizz then Buzz then i