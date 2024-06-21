def DFS(G, V, S, E):
    S.append(E)
    V[E] = True
    
    while S:
        current = S.pop()
        print(current, end=",")
        for i in G[current]:
            if not V[i[1]]:
                S.append(i[1])
                V[i[1]] = True

G = {
    1: [(1, 2, 0), (1, 3, 0)],
    2: [(2, 1, 0), (2, 7, 0)],
    3: [(3, 1, 0), (3, 6, 0), (3, 5, 0)],
    4: [(4, 7, 0), (4, 8, 0)],
    5: [(5, 3, 0), (5, 7, 0)],  
    6: [(6, 3, 0), (6, 8, 0)],
    7: [(7, 2, 0), (7, 5, 0), (7, 4, 0)],
    8: [(8, 4, 0), (8, 6, 0), (8, 8, 0)]
}

V = {i: False for i in G.keys()}

S = []

DFS(G, V, S, 1)