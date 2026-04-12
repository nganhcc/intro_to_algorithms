#C={("hihi.py", 12),("kkaa.cpp", 4),...}
#D={("hihi.py", "kkaa.cpp"),(),...}
#bai toan nay giai su cac files deu co phu thuoc lan nhau [important]

def build_job_graph(C, D):
    time = {}
    G = {}
    for (f, t) in C:
        G[f] = []
        time[f] = -t          # negate for longest path trick
    for (f1, f2) in D:
        G[f1].append(f2)
    return G, time

def dfs(Adj, s, parent, order):   # fix 4: no default args
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
    order.append(s)

def full_graph_exploration(Adj):
    parent = {v: None for v in Adj}
    order = []
    for v in Adj:
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
    return parent, order

def can_job_completed(G, order):
    rank = {v: i for i, v in enumerate(order)}
    for u in G:
        for v in G[u]:
            if rank[u] > rank[v]:
                return False
    return True

def try_to_relax(w, d, parent, u, v):
    if d[v] > d[u] + w[v]:       # fix 2: node weight w[v]
        d[v] = d[u] + w[v]
        parent[v] = u

def DAG_relaxation(Adj, w, topological_order):
    d = {v: float('inf') for v in Adj}     # fix 1: dict
    parent = {v: None for v in Adj}        # fix 1: dict
    # auxiliary s: every node with no incoming edge starts at 0
    for v in Adj:
        if d[v] == float('inf'):
            d[v] = w[v]                    # cost to start this node
    for u in topological_order:
        for v in Adj[u]:
            try_to_relax(w, d, parent, u, v)
    return d, parent

def min_time(C, D):
    G, time = build_job_graph(C, D)
    _, order = full_graph_exploration(G)   # fix 3: no G[0]
    order.reverse()                        # topological order
    if can_job_completed(G, order):
        d, _ = DAG_relaxation(G, time, order)
        return -min(d.values())            # negate back to positive
    else:
        return "Khong the hoan thanh nhiem vu"