class Graph:
    def __init__(self, nodes, adjacencyMatrix, vertexIndx):
        self.nodes = nodes
        self.adjacencyMatrix = adjacencyMatrix
        self.vertexIndx = vertexIndx
    def findAdjacencies(self, node, adjacentNodes = []):
        #get the row in the matrix
        for i in range(len(self.nodes)):
            nodeVertex = self.vertexIndx[node]
            if self.adjacencyMatrix[nodeVertex][i] == 1:
                adjacentNodes.append(self.nodes[i])

        return adjacentNodes
    def isConnected(self, node1, node2):
        nodeIdx1 = self.vertexIndx[node1]
        nodeIdx2 = self.vertexIndx[node2]

        return True if self.adjacencyMatrix[nodeIdx1][nodeIdx2] else False


if __name__ == '__main__':
    vertices = ['A','B','C', 'D', 'E']
    vertexIndx = {
        'A' : 0,
        'B' : 1,
        'C' : 2,
        'D' : 3,
        'E' : 4,
    }
    adjacencyMatrix = [
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [0, 0, 1, 1, 0],
    ]
    graps = Graph(vertices, adjacencyMatrix, vertexIndx)
    print(graps.findAdjacencies('E'))
    print(graps.isConnected('E', 'B'))