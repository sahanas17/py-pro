def palin( strr ):
    rev_strr = strr[ : : -1]
    if ( rev_strr == strr ):
        print( "Palindrome" )
    else:
        print( "Not Palindrome" )
print( "Palindrome checker" )
strr_input = str( input( "Enter the string: " ))
palin( strr_input )
