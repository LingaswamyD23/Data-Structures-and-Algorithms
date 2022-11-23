class Node:
    def __init__(self, val):
        self.val = val
        self.edgesList = []
    def connect(self, node):
        self.edgesList.append(node)

    def getAdjacentNode(self, edges = []):
        for edge in self.edgesList:
            edges.append(edge.val)
        return edges
    def isConnected(self, node):
        for edge in self.edgesList:
            if node.val ==edge.val:
                return True
        return False
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
    def addToGraph(self, node):
        self.nodes.append(node)

    def depthFirstTraversal(self, start, visited, topOrdering):
        if start in visited:
            return
        visited.add(start)
        print("Visitin node : ", start.val)
        for adjacency in start.edgesList:
            self.depthFirstTraversal(adjacency, visited, topOrdering)
        topOrdering.append(start.val)


    def topologicalSort(self):
        visited = set()
        topOrdering = []
        for node in self.nodes:
            self.depthFirstTraversal(node, visited, topOrdering)
        print(topOrdering[::-1])


if __name__ == '__main__':

    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')
    nodeF = Node('F')

    nodeA.connect(nodeC)
    nodeA.connect(nodeB)
    nodeB.connect(nodeD)
    nodeD.connect(nodeF)
    nodeE.connect(nodeF)
    nodeE.connect(nodeC)

    graph = Graph([nodeA, nodeB, nodeC, nodeD, nodeE])
    # for node in graph.nodes:
    #     print(node.val)
    #     for connectedNode in node.edgesList:
    #         print( f'node : {node.val} is connected to node : {connectedNode.val}')
    # print(nodeC.getAdjacentNode())
    # print(nodeD.isConnected(nodeB))
    graph.topologicalSort()