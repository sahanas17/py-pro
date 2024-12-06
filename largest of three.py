def max_num( num1, num2, num3 ) :
    if (( num1 > num2 ) and ( num1 > num3 )) :
        print( num1, ' is the largest' )
    elif (( num2 > num1 ) and ( num2 > num3 )) :
        print( num2, ' is the largest' )
    elif (( num3 > num1 ) and ( num3 > num2 )) :
        print( num3, ' is the largest' )
    else :
        print( "all the three numbers entered are equal" )
#end of max_num
print( "Largest of three" )
num1 = int( input( 'Enter first number : '))
num2 = int( input( 'Enter first number : '))
num3 = int( input( 'Enter first number : '))
max_num( num1, num2, num3 )

#comparison op in python - ll
