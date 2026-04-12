#for DAG, we use DAG relaxation algorithm to find shortest path
def dfs(Adj, s, parent=None, order=None):
    if parent is None:
        parent=[None for _ in Adj]
        parent[s]=s
        order=[]
    for v in Adj[s]:
        if parent[v] is None:
            parent[v]=s
            dfs[Adj, v, parent, order]
    order.append(s)
    return parent, order
#O(V+E)
#Graph exploration using dfs
def full_dfs(Adj):
    parent = [None for _ in Adj]
    order= []
    for v in Adj:
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
    return parent, order

def try_to_relax(Adj, w, d, parent, u, v):  #d: distances estimation
    if d[v]> d[u] + w[u, v]:
        d[v]=d[u]+w[u,v]
        parent[v]=u


def DAG_relaxation(Adj, w, s):  #construct shortest path to every vertices started from s
    _, order= dfs(Adj, s)
    order.reverse()
    d= [float('inf') for _ in Adj]
    parent=[None for _ in Adj]
    parent[s], d[s]= s, 0
    for u in order:
        for v in Adj[u]:
            try_to_relax(Adj, w, d, parent, u ,v)
    return d, parent

    
