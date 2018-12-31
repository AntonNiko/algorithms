#!/home/anton/anaconda3/bin/python

class Vertex:
    """Implementation of a Vertex in a Graph Abstract Data Type

    Args:
        key (Object): The value of the Vertex
    Attributes:
        id (Object): The identifier of the vertex, set by key argument

    """
    
    def __init__(self, key):
        self.id = key
        self.connections = {}

    def add_neighbor(self, neighbor_vert, weight=0):
        """Adds neighbor to the vertex

        Args:
            neighbor_vert (Object): The identifier for the neighboring vertex
            weight (int): The weight related to the edge connecting the two vertices
        """
        self.connections[neighbor_vert] = weight

    def get_neighbors(self):
        """Returns the id of all the vertice's neighbors

        Returns:
            (list): List containing if of vertice's neighbors
        """
        return self.connections.keys()

class Graph:
    """Implementation of Graph Abstract Data Type

    Attributes:
        vertices (dict): Dictionary of key, and Vertex object as elements
        numVertices (int): Number of Vertices in Graph
        numEdges (int): Number of dges in Graph
    """
    
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        self.numEdges = 0

    def add_vertex(self, key):
        """Adds a vertex to the graph

        Args:
            key (Object): The value and identifier of the vertex
        Returns:
            new_vertex (Vertex): The new generaed vertex
        """
        self.numVertices+=1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        """Returns all the vertices related to the graph

        Returns:
            (Vertex): Returns the vertex object found, or None if not found
        """
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def add_edge(self, origin_vert, dest_vert, cost=0):
        """Adds an edge (i.e connection) between two vertices that already exist
        in the graph. If any of the vertices do not exist, raises an exception.

        Args:
            origin_vert (Object): Identifier of the origin vertex (id attribute)
            dest_vert (Object): Identifier of destination vertex (id attribute)
            cost (int): An integer greater than or equal to zero, indicating
                        edge weight
        """
        if origin_vert not in self.vertices:
            raise Exception("The origin vertex does not exist")
        if dest_vert not in self.vertices:
            raise Exception("The destination vertex does not exist")
        self.vertices[origin_vert].add_neighbor(
            self.vertices[dest_vert], cost)
        self.numEdges+=1

    def get_vertices(self):
        return self.vertices.keys()

if __name__ == "__main__":
    pass

    
        
        
