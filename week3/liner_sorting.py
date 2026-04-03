#comparision sorting like: selection sorting, insertion sorting, merge sorting -> at least O(n log n) for sorting
#-> 
#Linear sorting

#Direct access array sorting: only apply for A having distinct, non-negative key
def direct_access_sort(A):
    u= 1+max([x.key for x in A])  #O(n) usuallt n<<u
    D= [None]*u   #O(u)   if u= O(n)  -> Linear sorting
    for x in A:
        D[x.key]=x
    i=0
    for k in range(u):
        if D[k] is not None:
            A[i]=D[k]
        i+=1
#Problem: can't solve duplicates
#-> counting sort
def counting_sort_1(A): #way 1
    u=1+max([x.key for x in A])
    D=[[]] *u    #if u=O(n) -> linear sorting but can solve duplicates
    for x in A:
        D[x.key].append(x)
    i=0
    for chain in range (D):
        for x in chain:
            A[i]=x
            i+=1
def counting_sort_2(A): #way2
    u=1+max([x.key for x in A])
    D=[0]*u
    for x in A:
        D[x.key]+=1
    for i in range (1,u,1): #count cummulative sum
        D[i]+=D[i-1]
    
    for x in list(reversed(A)):
        A[D[x.key]-1]=x
        D[x.key]-=1
#what if u is too large -> need break integer into parts then sorting each part
#if u<= n^c  -> linear sort
def radix_sort(A):
    n=len(A)  #O(n) find max item in A
    u=1+max([x.key for x in A]) #O(u) 
    c= 1 + (u.bit_length()//n.bit_length())  #x.bit_length()= log2(x) : number of bits to represents x -> c = 1+ log n(u) -> number of column
    #build tuple digits
    '''
    x in A:
    D= [
    {key:"", item=x, digits:[1,4,6,3]},   key is used for count sort
    {key:"", item=x, digits:[1,4,6,3]},
    {key:"", item=x, digits:[1,4,6,3]},
    ]
    '''
    class Obj(): pass
    D=[Obj() for x in A]   
    for i in range(n):  #O(nc) make digit tuples
        D[i].digits=[]
        D[i].item=A[i]
        high=A[i].key
        for j in range (c):  #O(n) make digit tuple
            high, low= divmod(high, n)
            D[i].digits.append(low)
    for j in range(c):  #O(nc) sort each digit
        for i in range(n): #O(n) assign key i to tuples
            D[i].key=D[i].digits[j]
        counting_sort_1(D)  #O(n) sort on digit i
    for i in range(n):  #O(n) 
        A[i]=D[i].item
    
    








