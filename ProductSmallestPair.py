'''def ProductSmallestPair(sum, arr)
The function accepts an integers sum and an integer array arr of size n. Implement the function to find the pair, (arr[j], arr[k]) where j!=k, Such that arr[j] and arr[k] are the least two elements of array (arr[j] + arr[k] <= sum) and return the product of element of this pair
NOTE
    Return -1 if array is empty or if n<2
    Return 0, if no such pairs found
    All computed values lie within integer range
Example
Input
sum:9
size of Arr = 7
Arr:5 2 4 3 9 7 1
Output
2'''

def ProductSmallestPair(sum, arr):
    size = len( arr )
    if size < 2:
        return "-1"
    for i in range( 0, size ):
        for j in range( i + 1, size):
            if( arr[i] >= arr[j]):
                arr[i], arr[j] = arr[j], arr[i]    
    print( arr )
    if ( arr[0] != arr[1] and ((arr[0] + arr[1]) <= sum)):
        print( "Product: ", arr[0] * arr[1])
    else:
        print( "0" )
ProductSmallestPair( 9, [9, 8, 3, -7, 3, 9] )


        
