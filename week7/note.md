*SSSP problem: single source shortest path in general graph(potentially cycle, negative weights)

**Preoblem 1: reachable from start s: first we use bfs, or dfs to find all vertices that are reachable from s -> now we have |V| = O(|E|)
O(V*(V+E))  problem -> O(V.E)

**problem2: simple shortest paths
- claim1: if shortest path distance delta(s,v) is finite-> threre are exists simple shortest path from s->v
proof: image: claim1.png: Neu s-> v co simple shortest path finite, Neu cycle la negative cycle-> impossible
neu cycle =0 hoawc positive integer -> ta co the xoa cycle do -> fewer cycle path 

simple paths have at most |V|-1 edges