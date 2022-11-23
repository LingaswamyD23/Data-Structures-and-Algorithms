class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
    def findAdjacentNodes(self, node, adjacentNodes = []):
        for edge in self.edges:
            nodeIdx = edge.index(node) if node in edge else -1
            if nodeIdx>-1:
                adjacentNode = edge[1] if nodeIdx == 0 else edge[0]
                adjacentNodes.append(adjacentNode)
        return adjacentNodes
    def isConnected(self, node1, node2):
        for edge in self.edges:
            if node1 in edge and node2 in edge:
                return True
        return False


if __name__ == '__main__':
    vertices = ['A','B','C', 'D', 'E']
    edges = [
        ['A','B'],
        ['A', 'D'],
        ['B', 'C'],
        ['C', 'D'],
        ['C', 'E'],
        ['D', 'E']
    ]
    grap = Graph(vertices, edges)
    print(grap.findAdjacentNodes('C'))
    print(grap.isConnected('A', 'E'))
    