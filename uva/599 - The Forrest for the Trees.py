def find_set(u):
    if u != tree[u]:
        return find_set(tree[u])
    return u

def union_set(u, v):
    u_p = find_set(u)
    v_p = find_set(v)
    if u_p != v_p:
        if rank[u_p] > rank[v_p]:
            tree[v_p] = u_p
            rank[u_p] += rank[v_p]
        else:
            tree[u_p] = v_p
            rank[v_p] += rank[u_p]

t = int(input().strip())
for _ in range(t):
    tree = []
    rank = []
    index = 0
    mapped = dict()
    while True:
        edge = input().strip()
        if edge[0] == "*":
            break
        a = edge[1]
        b = edge[3]
        if a not in mapped:
            mapped.setdefault(a, index)
            tree.append(index)
            rank.append(1)
            index += 1
        if b not in mapped:
            mapped.setdefault(b, index)
            tree.append(index)
            rank.append(1)
            index += 1
        union_set(mapped[a], mapped[b])
    nodes = list(map(str, input().split(",")))
    res_tree = 0
    res_acorn = 0
    for node in nodes:
        if node not in mapped:
            res_acorn += 1
        elif tree[mapped[node]] == mapped[node] and rank[mapped[node]] > 1:
            res_tree += 1
    print("There are %d tree(s) and %d acorn(s)." % (res_tree, res_acorn))


