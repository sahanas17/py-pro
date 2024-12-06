def checkPassword(s, n):
    if (n < 4) :
        return 0
    if(s[0].isdigit == True):
        return 0
    cap = 0
    no = 0
    for i in range(n):
        if(s[i].isupper()):
            cap += 1
        if (s[i].isdigit()):
            no += 1   
        if (s[i] == " " or i == "/"):
            return 0
    if cap > 0 and no > 0:
        return ( "Valid" )
    else:
        return ( "Invalid" )
    
#
s = input("Enter the password: ")
n = len(s)
print(checkPassword(s, n))
