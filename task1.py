def analyze_tree(n, log):
    tree = [[] for _ in range(n)]
    stack = []
    current_node = 0
    node_count = 1

    for char in log:
        if char == '0':
            stack.append(current_node)
            tree[current_node].append(node_count)
            tree[node_count].append(current_node)
            current_node = node_count
            node_count += 1
        elif char == '1':
            current_node = stack.pop()

    def bfs(start):
        dist = [-1] * n
        dist[start] = 0
        queue = [start]
        head = 0
        farthest_node = start

        while head < len(queue):
            node = queue[head]
            head += 1
            for neighbor in tree[node]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
                    farthest_node = neighbor

        return farthest_node, dist

    farthest_node, _ = bfs(0)
    opposite_node, dist_from_farthest = bfs(farthest_node)
    diameter = max(dist_from_farthest)
    radius = (diameter + 1) // 2
    center = diameter % 2 + 1

    return center, radius, diameter


n = 15
log = "0011001011010010101100011101"

result = analyze_tree(n, log)
print(*result)
