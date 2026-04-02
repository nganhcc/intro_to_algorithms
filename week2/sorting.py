#build set interface take O(n log n)

def selection_sort(A):  #maintains and grows a subset of the largest i items in sorted order -> in-place
    for i in range(len(A)-1, 0 ,-1):
        m=i
        for j in range(i):
            if A[j]>A[m]:
                m=j
        A[i], A[m] = A[m], A[i]
def insertion_sort(A): #maintains and grows a subset of first i items in sorted order  -> stable, in-place
    for i in range(1, len(A)):
        j=i
        while j>0 and A[j]<A[j-1]:
            A[j], A[j-1] =A[j-1], A[j]
            j-=1

def merge(X,Y):  ##X, Y are already sorted
    result=[]
    while len(X)!=0 or len(Y)!=0:
        if (len(X)==0):
            result.append(Y.pop(0))
        elif (len(Y)==0):
            result.append(X.pop(0))
        elif (len(X)!=0 and len(Y)!=0):
            if (X[0]<=Y[0]):
                result.append(X.pop(0))
            else:
                result.append(Y.pop(0))
    return result

def merge_sort(A):
    if len(A)==1:return A
    mid= len(A)//2   #left_A= A[0:mid] , right_A=A[mid, len(A)]
    left_A=merge_sort(A[0:mid])
    right_A=merge_sort(A[mid:len(A)])
    return merge(left_A, right_A)

arr=[3,6,2,8,3,5,7,1,2,9,10,3,6,8]
print(merge_sort(arr))


