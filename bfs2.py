def BFS(G, e):
    Q = [e]
    V = {}  # Use dictionary to track visited nodes
    for i in G.keys():
        V[i] = False
    V[e] = True
    
    while len(Q) != 0:
        curr = Q.pop(0)
        print(curr, end=", ")
        for i in G[curr]:
            if not V[i[1]]:
                Q.append(i[1])
                V[i[1]] = True    

Graph = {
    1: [(1, 2, 0), (1, 3, 0)],
    2: [(2, 1, 0), (2, 7, 0)],
    3: [(3, 1, 0), (3, 6, 0), (3, 5, 0)],
    4: [(4, 7, 0), (4, 8, 0)],
    5: [(5, 3, 0), (5, 7, 0)],  
    6: [(6, 3, 0), (6, 8, 0)],
    7: [(7, 2, 0), (7, 5, 0), (7, 4, 0)],
    8: [(8, 4, 0), (8, 6, 0), (8, 8, 0)]
}

print("Result: ")
BFS(Graph, 1)