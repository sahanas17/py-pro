def palin( strr ):
    left = 0
    right = len(strr) -1

    if ( strr[left] != strr[right]):
        return print( "Not palindrome" )
        left += 1
        right -= 1
    return print( "Palindrome")
print( "Palindrome checker without built-in functions" )
usr_inp = str( input( "Enter the string: " ))
palin(usr_inp)


