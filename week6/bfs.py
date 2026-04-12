#bfs: find shortest path in unweighted graph

def bfs(Adj, s):   #Adj: adjacency list, s: start
    parents=[None for v in Adj]  #O(V): use hashtable if unlabeled
    parents[s]=s 
    level=[[s]]
    while 0<len(level[-1]):
        level.append([])   #amortized O(1): use dynamic array
        for u in level[-2]:
            for v in Adj[u]:  #O(Adj(u))
                if parents[v] is None:
                    level[-1].append(v)  #O(1) amortized
                    parents[v]=u
    return parents
# inner loop: for v in Adj(u) =run through all edges  -> O(E)
#+O(V) for parents return 
# O(V+E) for bfs

#shortest path for unweighted graph
def unweighted_shortest_path(Adj, s, t):
    parents= bfs(Adj, s)  #O(V+E)
    if parents[t] is None:
        return None
    path=[t]
    i=t
    while i!=s:
        i=parents[i]
        path.append(i)
    return path[::-1] #return reversed path
    