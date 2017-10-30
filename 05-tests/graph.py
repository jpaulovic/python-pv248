class GraphException(Exception):
    pass


class Graph:
    def __init__(self):
        """Create empty oriented graph"""
        self._nodes = {}

    def add_node(self, node_id):
        """
        Create new_node in the graph. Raises GraphException 
        when duplicate node_id already exists"""
        if node_id in self.nodes():
            raise GraphException("Duplicate node_id used")
        self._nodes[node_id] = []

    def add_edge(self, node_from, node_to):
        """
        Add edge to the graph. 
        Raises GraphException when duplicate edge exists
        """
        if node_from not in self.nodes() or node_to not in self.nodes():
            raise GraphException("node does not exist")
        if node_to in self._nodes[node_from]:
            raise GraphException("Edge already exists")
        self._nodes[node_from].append(node_to)

    def has_key(self, node):
        return self.nodes().__contains__(node)

    def has_edge(self, node_from, node_to):
        """
        Checks is edge exists.

        Raises GraphException if node_from and node_to doesn't exist.
        Returns True if edge exists
        Retrun False if edge doesn't exist.
        """
        if node_to not in self.nodes():
            raise GraphException("node_to does not exist")
        if node_from not in self.nodes():
            raise GraphException("node_from does not exist")
        if node_to in self._nodes[node_from]:
            return True
        return False

    def has_path(self, node_from, node_to):
        """
        Checks is path exists.

        Raises GraphException is node_from and node_to doesn't exists.
        Returns True if path exists
        Retrun False if path doesn't exist.
        """
        if node_to not in self.nodes():
            raise GraphException("node_to does not exist")
        if node_from not in self.nodes():
            raise GraphException("node_from does not exist")
        path = self.find_shortest_path(node_from, node_to)
        if not path:
            return False
        return True

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.nodes():
            return None
        shortest = None
        for node in self._nodes[start]:
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def nodes(self):
        """Return list on nodes ids"""
        return self._nodes.keys()

    def node_count(self):
        "Return count of nodes"
        return len(self._nodes)
