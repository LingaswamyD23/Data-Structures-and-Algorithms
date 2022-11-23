class Node:
    def __init__(self, val):
        self.val = val
        self.edgesList = []
    def connect(self, node):
        self.edgesList.append(node)
        node.edgesList.append(self)
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



if __name__ == '__main__':

    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')

    nodeA.connect(nodeB)
    nodeA.connect(nodeD)
    nodeB.connect(nodeC)
    nodeC.connect(nodeD)
    nodeC.connect(nodeE)
    nodeD.connect(nodeE)

    graph = Graph([nodeA, nodeB, nodeC, nodeD, nodeE])
    # for node in graph.nodes:
    #     print(node.val)
    #     for connectedNode in node.edgesList:
    #         print( f'node : {node.val} is connected to node : {connectedNode.val}')
    print(nodeC.getAdjacentNode())
    print(nodeD.isConnected(nodeB))