#write a recursive function to caculate the sum of first n natural number

def sum(n):
    if( n==0 or n==1):
        return 1
    else:
        return n + sum(n-1)
    
print(sum(4))

def cal(n):
    if(n==0):
        return 0
    return cal(n-1) + n
print(cal(4))