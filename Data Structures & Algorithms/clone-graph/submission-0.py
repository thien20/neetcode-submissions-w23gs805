"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # deep copy is creating a new entirely object (same val or its connection), which is independent from the org one
        # we need a dictionary to store the org val as the key and the copy node as the value
        # meta data of that should be like this: 
        # dic = { NodeA: Node(node.val) }
        if node is None:
            return None
        dic = {node: Node(node.val) }

        # analyze the cases:
        # bfs should work
        dq = deque([node])
        while dq:
            curr_node = dq.popleft()

            for neighbor in curr_node.neighbors:
                if neighbor not in dic:
                    dic[neighbor] = Node(neighbor.val)
                    dq.append(neighbor)
                dic[curr_node].neighbors.append(dic[neighbor])
        return dic[node]

                








