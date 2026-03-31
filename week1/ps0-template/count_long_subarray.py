def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    if len(A)==0:
        return 0
    ##################
    count = 1
    temp=[A[0]]
    max=1
    for i in range (1,len(A),1):
        if len(temp)==0 or (len(temp)!=0 and A[i]>temp[len(temp)-1]):
            temp.append(A[i])
            if len(temp)==max:
                count+=1
            if len(temp)>max:
                max+=1
                count=1
        else:
            temp=[A[i]]
    ##################
    return count
