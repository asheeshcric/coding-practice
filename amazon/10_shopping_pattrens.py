# Inputs
products_nodes = 6
products_edges = 6
products_from = [1, 1, 2, 2, 3, 4]
products_to = [2, 3, 3, 4, 4, 5]


def create_graph(products_from, products_to):
    # Creates an undirected graph
    graph = dict()
    for i, prod in enumerate(products_from):
        prod_to = products_to[i]
        if prod not in graph.keys():
            graph[prod] = [products_to[i]]
        else:
            graph[prod].append(products_to[i])

        if prod_to not in graph.keys():
            graph[prod_to] = [prod]
        else:
            graph[prod_to].append(prod)

    return graph


graph = create_graph(products_from, products_to)

trios = dict()
for node in graph.keys():
    for first_neigh in graph[node]:
        is_node_present = 1 if node in graph[first_neigh] else 0
        for second_neigh in graph[first_neigh]:
            if second_neigh == node:
                # Avoid two node loops
                continue
            if node in graph[second_neigh]:
                # We found a trio
                new_trio = [node, first_neigh, second_neigh]
                if sum(new_trio) not in trios:
                    # To avoid duplicate trios
                    trios[sum(new_trio)] = sorted(new_trio)

print(trios)

if len(trios) == 0:
    print(-1)
else:
    min_value = float('inf')
    for _, trio in trios.items():
        outside_trio = set()
        for node in trio:
            for neigh in graph[node]:
                if neigh not in trio:
                    outside_trio.add(neigh)
        
        min_value = min(len(outside_trio), min_value)

    print(min_value)
