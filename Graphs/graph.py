class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print(self.graph_dict)
    def get_paths(self, start, end, path = []):
        path = path + [start]
        paths = []
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths
    def get_shortest_path(self, start,end, path = []):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                short_path = self.get_shortest_path(node, end, path)
                if short_path:
                    if shortest_path == None or len(short_path) < len(shortest_path):
                        shortest_path = short_path

        return shortest_path





if __name__ == '__main__':
    routes = [
        ("mumbai", "paris"),
        ("mumbai", "dubai"),
        ("paris", "dubai"),
        ("paris", "newyark"),
        ("dubai", "newyark"),
        ("newyark", "toronto"),
    ]
    route_graph = Graph(routes)
    print(route_graph.get_paths('mumbai', 'newyark'))
    print(route_graph.get_shortest_path('mumbai', 'newyark'))