ORD_A = ord('a')


def lower_order(c):
        return ord(c)-ORD_A


def count_anagram_substrings(T, S):
        '''
        Input:  T | String
                S | Tuple of strings S_i of equal length k < |T|
        Output: A | Tuple of integers a_i:
                | the anagram substring count of S_i in T
        '''
        ##################
        m, n, k = len(T), len(S), len(S[0])
        F = [0]*26  # frequency table for each substring size of k
        D = {}
        for i in range(m):
                c_order = lower_order(T[i])
                F[c_order] += 1
                if i >= k:
                        old_c_order = lower_order(T[i-k])
                F[old_c_order] -= 1
                if i >= k-1:
                        key = tuple(F)
                if key in D:
                        D[key] += 1
                else:
                        D[key] = 1
        A=[0]*n
        for i in range(n):
                F=[0]*26
                s=S[i]
                for j in range(k):
                        c_order=lower_order(s[j])
                        F[c_order]+=1
                key=tuple(F)
                if key in D:
                        A[i]=D[key]
        ##################
        return tuple(A)
