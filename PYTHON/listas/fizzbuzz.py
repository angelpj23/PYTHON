num = range(100)

for n in num:
    if n % 5 == 0 and n % 7 == 0:
        print ("fizzbuzz")
    elif n % 5 ==0:
        print ("fizz")
    elif n % 7 == 0:
        print ("buzz")
    else:
        print (n)