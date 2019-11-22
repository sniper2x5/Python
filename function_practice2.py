
def occ (a,b):
    """occ (a,b) - takes in 2 strings and returns how many times b occurs in a"""
    #Global Variables
    count = 0
    start=0
    while True:
        #Calculations for ocurrences
        search = a.find(b,start)
        if search == -1:
            break
        else:
            count +=1
            start = search+1
    return count
print occ("banana", "ana")
    
    
    