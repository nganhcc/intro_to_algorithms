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

#DAG: directed acyclic graph: no cycle -> topological sort via DFS
