def fib(n):
    a, b, c = 0,1,0
    for i in range(n):
        a = b
        b = c
        c = a + b
        print( c, end = " " )                
print( "This program prints the fibonacci series" )
fib(5)

