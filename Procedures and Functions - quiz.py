def Q1():
    print ("when did world war one start?")
    print ("1.1915")
    print ("2.1910 ")
    print ("3.1914")
    print ("4.1900")
    Q1A = input("/")
    
    if Q1A == "3":
        print ("correct")
    else:
        print ("wrong")

def Q2():
    print ("How many countries make up Africa?")
    print ("1.54")
    print ("2.46 ")
    print ("3.67")
    print ("4.49")
    Q1A = input("/")
    
    if Q1A == "1":
        print ("correct")
    else:
        print ("wrong")

#---------------   
print ("Quiz time")
print ("what difficult do you want")
print ("1 = easy")
print ("2 = hard")
Dif = input("/")

if Dif == "1":
    Q1()
    
    
elif Dif == "2":
    Q2()

else:
    print ("please pick 1 or 2")
