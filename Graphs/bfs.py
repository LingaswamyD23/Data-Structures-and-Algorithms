class Node:
    def __init__(self, value, edgeList = []):
        self.value = value
        self.edgeList = edgeList
    def connect(self, node):
        self.edgeList.append(node)
        node.edgeList.append(self)
    def getAdjacentNode(self, edges= []):
        for edge in self.edgesList:
            edges.append(edge.value)
        return edges

    def isConnected(self, node):
        for edge in self.edgeList:
            if edge.value == node.value:
                return True
        return False

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
    def addToGraph(self, node):
        self.nodes.append(node)

    def breadthFirstTraversal(self, startNode, endNode):
        queue = [startNode]
        visitedNodes = set()
        visitedNodes.add(startNode)
        while len(queue)>0:
            node = queue.pop(0)
            if node.value == endNode.value:
                print(node.value)
                print('Found it..!')
                return
            for adjacency in node.edgeList:
                if adjacency not in visitedNodes:
                    queue.append(adjacency)
                    visitedNodes.add(adjacency)
            print(node.value)





if __name__ == '__main__':
    DFW = Node('DFW')
    JFK = Node('JFK')
    LAX = Node('LAX')
    HNL = Node('HNL')
    SAN = Node('SAN')
    EWR = Node('EWR')
    BOS = Node('BOS')
    MIA = Node('MIA')
    MCO = Node('MCO')
    PBI = Node('PBI')



    graph = Graph(nodes=[DFW, JFK, LAX, HNL, SAN, EWR, BOS, MIA, MCO, PBI])

    DFW.connect(LAX)
    DFW.connect(JFK)
    LAX.connect(HNL)
    LAX.connect(EWR)
    LAX.connect(SAN)
    JFK.connect(BOS)
    JFK.connect(MIA)
    MIA.connect(MCO)
    MCO.connect(PBI)
    MIA.connect(PBI)

    graph.breadthFirstTraversal(DFW, MIA)



