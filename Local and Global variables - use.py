V = "this is a Global variable"# this can be used anywhere
X = "Global Can be used anywhere"#this also can

def Local():
    V = "This is a Local variable"
    print (V)#this can be used within this def to print the v above out
    print (X)#this shows that it can be used anwhere
    
print (V)
Local()
