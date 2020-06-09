"""
Simple graph implementation
"""
from util import Stack, Queue

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue to store all unseen vertices and
        # create a set to store all seen/touched verts
        unseen_verts = Queue()
        seen_verts = set()

        # initialize the queue by adding the input vertex (starting vertex)
        unseen_verts.enqueue(starting_vertex)

        # while there are items in the queue...
        while unseen_verts.size() > 0:

            # grab the current vertex
            current_vert = unseen_verts.dequeue()

            # if the current vertex is not already in the seen_verts set,
            # print it and add it to the seen_verts set
            if current_vert not in seen_verts:
                print(current_vert)
                seen_verts.add(current_vert)

                # then add all of the current vertex's neighbors to the queue
                for neighbor in self.get_neighbors(current_vert):
                    unseen_verts.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack to store all unseen vertices and
        # create a set to store all seen/touched verts
        unseen_verts = Stack()
        seen_verts = set()

        # initialize the stack by adding the input vertex (starting vertex)
        unseen_verts.push(starting_vertex)

        # while there are items in the stack...
        while unseen_verts.size() > 0:

            # grab the current vertex
            current_vert = unseen_verts.pop()

            # if the current vertex is not already in the seen_verts set,
            # print it and add it to the seen_verts set
            if current_vert not in seen_verts:
                print(current_vert)
                seen_verts.add(current_vert)

                # then add all of the current vertex's neighbors to the stack
                for neighbor in self.get_neighbors(current_vert):
                    unseen_verts.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        def dft_rec_helper(starting_vertex):
            # if the current vertex is not already in the seen_verts set,
            # print it and add it to the seen_verts set
            if starting_vertex not in seen_verts:
                print(starting_vertex)
                seen_verts.add(starting_vertex)
                # then invoke this same helper function on each
                # of the current vertex's neighbors, recursively
                for neighbor in self.get_neighbors(starting_vertex):
                    dft_rec_helper(neighbor)

        # create a set to store all seen/touched vertices and
        # run the dft_rec_helper() function on the input vertex (starting vertex)
        seen_verts = set()
        dft_rec_helper(starting_vertex)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue to store all unseen verts
        unseen_verts = Queue()
        # create a set to store all seen/touched verts
        seen_verts = set()
        # create a dictionary to store key-value pairs for each seen vertex
        # and the list of paths to it from the starting vertex
        paths = dict()

        # initialize the queue by adding the input vertex (starting vertex) and
        # initialize the dict by adding an empty list at the input vertex key
        unseen_verts.enqueue(starting_vertex)
        paths[starting_vertex] = []

        # while there are items in the queue...
        while unseen_verts.size() > 0:

            # grab the current vertex
            current_vert = unseen_verts.dequeue()

            # if the current vertex is not already in the seen_verts set,
            # add it to the seen_verts set
            if current_vert not in seen_verts:
                seen_verts.add(current_vert)
                
                # for each of the current vertex's neighbors...
                for neighbor in self.get_neighbors(current_vert):

                    # if the current neighbor is the destination vertex, update the path
                    # from the starting vertex to the current neighbor, then return this path
                    if neighbor == destination_vertex:
                        current_path = paths[current_vert][:]
                        current_path.append(current_vert)
                        current_path.append(neighbor)
                        return current_path

                    # add all of the current vertex's neighbors to the queue
                    unseen_verts.enqueue(neighbor)

                    # grab the current path up until this point,
                    # then add the current vertex to the end
                    path_till_now = paths[current_vert][:]
                    path_till_now.append(current_vert)

                    # lastly, store the updated path to the neighbor in the paths dict
                    paths[neighbor] = path_till_now
        
        # if a path is not found, print an error message and return nothing
        print('bfs error: \nSorry, a path between these two vertices could not be found')
        return

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack to store all unseen verts
        unseen_verts = Stack()
        # create a set to store all seen/touched verts
        seen_verts = set()
        # create a dictionary to store key-value pairs for each seen vertex
        # and the list of paths to it from the starting vertex
        paths = dict()

        # initialize the stack by adding the input vertex (starting vertex) and
        # initialize the dict by adding an empty list at the input vertex key
        unseen_verts.push(starting_vertex)
        paths[starting_vertex] = []

        # while there are items in the stack...
        while unseen_verts.size() > 0:

            # grab the current vertex
            current_vert = unseen_verts.pop()

            # if the current vertex is not already in the seen_verts set,
            # add it to the seen_verts set
            if current_vert not in seen_verts:
                seen_verts.add(current_vert)
                
                # for each of the current vertex's neighbors...
                for neighbor in self.get_neighbors(current_vert):

                    # if the current neighbor is the destination vertex, update the path
                    # from the starting vertex to the current neighbor, then return this path
                    if neighbor == destination_vertex:
                        current_path = paths[current_vert][:]
                        current_path.append(current_vert)
                        current_path.append(neighbor)
                        return current_path

                    # add all of the current vertex's neighbors to the stack
                    unseen_verts.push(neighbor)

                    # grab the current path up until this point,
                    # then add the current vertex to the end
                    path_till_now = paths[current_vert][:]
                    path_till_now.append(current_vert)

                    # lastly, store the updated path to the neighbor in the paths dict
                    paths[neighbor] = path_till_now
        
        # if a path is not found, print an error message and return nothing
        print('dfs error: \nSorry, a path between these two vertices could not be found')
        return

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def dfs_rec_helper(starting_vertex, destination_vertex, path_till_now):
            # if the current vertex is not already in the seen_verts set, add it
            if starting_vertex not in seen_verts:   
                seen_verts.add(starting_vertex)
                # if a path has been found, stop the recursion by returning nothing
                if success:
                    return
                # if the starting vert equals the destination vert, update the path
                # up until this point by adding the starting vertex to the end
                # then add the path to the dict
                elif starting_vertex == destination_vertex:
                    current_path = path_till_now[:]
                    current_path.append(starting_vertex)
                    paths[destination_vertex] = current_path
                else:
                    # otherwise, invoke this same helper function on each
                    # of the current vertex's neighbors, recursively
                    for neighbor in self.get_neighbors(starting_vertex):
                        new_path = path_till_now[:]
                        new_path.append(starting_vertex)
                        dfs_rec_helper(neighbor, destination_vertex, new_path)

        # create a boolean flag to deteremine when the path to the destination
        # vertex has been found so we can stop the recursion
        success = False
        # create a set to store all seen/touched vertices
        seen_verts = set()
        # create a dictionary to store key-value pairs for each seen vertex
        # and the list of paths to it from the starting vertex
        paths = dict()

        # run the dfs_rec_helper() function on the input vertices with
        # an empty list passed in as the path_till_now
        dfs_rec_helper(starting_vertex, destination_vertex, [])

        # return the full path from the starting vertex to the destination vertex
        return paths[destination_vertex]



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
