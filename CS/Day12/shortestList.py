import heapq

class Graph():

    def shortest_path(self, G, start, end):
        def flatten(L):       # Flatten linked list of form [0,[1,[2,[]]]]
          while len(L) > 0:
             yield L[0]
             L = L[1]

        q = [(0, start, ())]  # Heap of (cost, path_head, path_rest).
        visited = set()       # Visited vertices.
        while True:
            (cost, v1, path) = heapq.heappop(q)
            if v1 not in visited:
                visited.add(v1)
            if v1 == end:
                flat_path = list(flatten(path))[::-1] + [v1]
                print("Path: %s" % flat_path)
                return cost
            path = (v1, path)
            for v2, cost2 in G[v1].items():
                if v2 not in visited:
                    heapq.heappush(q, (cost + cost2, v2, path))



if __name__ == "__main__":
    # NODE: [{INDEX: WEIGHT}]
    data = {
        0: {1:4,7:8},
        1: {0:4,2:8,7:11},
        2: {1:8,3:7,5:4,8:2},
        3: {2:7,5:14,4:9},
        4: {3:9,5:10},
        5: {4:10,3:14,2:4,6:2},
        6: {5:2,8:6,7:1},
        7: {6:1,8:7,1:11,0:8},
        8: {7:7,6:6,2:2}
    }
    # print(data)
    graph_service = Graph()

    dist = []
    for node in data.keys():
        cost = graph_service.shortest_path(data,0,node)
        dist.append(cost)
    print("Vertex \tDistance from Source")
    for node in data.keys():
        print("%s \t %s " % (node, dist[node]))
