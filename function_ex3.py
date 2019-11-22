

def persistence(n):
    '''persistence (n) - takes in a number,calculates and returns the persistence'''
    #Variables
    n=int(n)
    count=0
    base=1
    #Calculations until number is single digit and tracks instances
    while len(str(n))>1:
        for x in str(n):
            base*=int(x)
        n=base
        count+=1
    return count
print persistence(427)
    
        
