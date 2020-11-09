def In():
    name = input("what is you first name?")
    sname = input("what is your second name?")
    age = input("what is your age?")
    return name, sname, age
    
def W():
    name, sname, age=In()
    lsname = (sname[0:3])
    lname = (name[0])
    print ("your username would be:", lsname+lname + age)
    
#---------------------------
print("--------------------")
print ("user name generator")
print("--------------------")
W()
