def In():#this takes in the information to creat a username
    name = input("what is you first name?")
    sname = input("what is your second name?")
    age = input("what is your age?")
    return name, sname, age
    
def W():#this takes what they picked and combined then for the username
    name, sname, age=In()
    lsname = (sname[0:3])
    lname = (name[0])
    print ("your username would be:", lsname+lname + age)
    
#---------------------------beginning
print("--------------------")
print ("user name generator")
print("--------------------")
W()
