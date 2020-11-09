V = "this is a Global variable"
X = "Global Can be used anywhere"

def Local():
    V = "This is a Local variable"
    print (V)
    print (X)
    
print (V)
Local()
