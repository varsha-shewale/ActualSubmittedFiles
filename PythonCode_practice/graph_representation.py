
class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self,value,from_node, to_node):
        self.value = value
        self.from_node = from_node
        self.to_node = to_node

class Graph(object):
    def __init__(self, nodes = [], edges = []):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self,value):
        new_node = Node(value)
        self.nodes.append(new_node)

    def insert_edge(self, value, from_node_val,to_node_val):
        from_node_found = None
        to_node_found = None
        #traverse through nodes list to locate from_node, to_node
        for n in self.nodes:
            if n.value == from_node_val:
                from_node_found = n
            if n.value == to_node_val:
                to_node_found = n
        #if from_node wasn't in node list then create this node
        if from_node_found == None:
            from_node_found = Node(from_node_val)
            self.nodes.append(from_node_found)

        #if to_node wasn't in node list then create this node
        if to_node_found == None:
            to_node_found = Node(to_node_val)
            self.nodes.append(to_node_found)

        new_edge = Edge(value,from_node_found,to_node_found)
        new_edge.from_node = from_node_found
        new_edge.to_node = to_node_found

        from_node_found.edges.append(new_edge)
        to_node_found.edges.append(new_edge)
        self.edges.append(new_edge)


    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        edge_list = []
        for edge in self.edges:
            edge_val = edge.value
            edge_from_val = edge.from_node.value
            edge_to_val = edge.to_node.value
            edge_list.append((edge_val,edge_from_val,edge_to_val))

        return edge_list

    def get_undirected_adjacency_list(self):
        #adjacency_list takes one node at a time and creates a list of
        # its neighouring nodes along with corresponding edge values.

        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""

        #create empty adjancency_list
        adj_list = []
        #trace each node
        for n in self.nodes:
            n_e_list = []
            for e in n.edges:
                #create a tuple (neighbor_node_val, edge_val) for each neighbor node
                #append this tuple to the list for this specific main node
                if n.value == e.from_node.value:
                    n_e_list.append(tuple([e.to_node.value,e.value]))
                elif n.value == e.to_node.value:
                    n_e_list.append(tuple([e.from_node.value,e.value]))
            adj_list.append(n_e_list)

        return adj_list

    def find_graph_max_index(self):
        max_index = -1
        if len(self.nodes):
            for n in self.nodes:
                if n.value > max_index:
                    max_index = n.value
        return max_index

    def get_adjacency_list(self):
        max_index = self.find_graph_max_index()
        adj_list = [None]*max_index
        for edge_obj in self.edges:
            if adj_list[edge_obj.from_node.value]:
                adj_list[edge_obj.from_node.value].append((edge_obj.to_node.value,edge_obj.value))
            else:
                adj_list[edge_obj.from_node.value] = [(edge_obj.to_node.value,edge_obj.value)]
        return adj_list

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        max_index = self.find_graph_max_index()
        adj_matrix = [[0 for c in range(max_index+1)] for r in range(max_index+1)]

        for edge_obj in self.edges:
            adj_matrix[edge_obj.from_node.value][edge_obj.to_node.value] = edge_obj.value
        return adj_matrix



graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print graph.get_edge_list()
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print graph.get_adjacency_list()

print graph.get_undirected_adjacency_list()

# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print graph.get_adjacency_matrix()