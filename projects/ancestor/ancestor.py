from graph import Graph
from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    # create two new dicts to store the child-parent key-value pairs and depths
    parents = dict()
    depths = dict()

    # for each tuple in the input array (ancestors), deconstruct the key-value pair
    # into parent and child nodes then store them in the parents dict accordingly
    for key_value in ancestors:
        parent, child = key_value

        # if the child is not already in the parents dict, add the parent
        # node as the value at the child node in the parents dict
        if child not in parents:
            parents[child] = [parent]
        else:
            # otherwise, if child is already in the parents dict, append its parent
            # node to the end of the list at the child node in the parents dict
            parents[child].append(parent)

        # if parent is not already in the parents dict, add an empty list
        # as the value at the parent node in the parents dict
        if parent not in parents:
            parents[parent] = []

    # this function assigns a depth (in generations) for
    # each ancestral node, beginning at the starting node
    def assign_depths(starting_node, previous_depth):
        # for each parent in the parents dict at the starting node...
        for parent in parents[starting_node]:
            
            # if the current parent's depth is not already in the depths dict, add the
            # parent as the value at the current depth in the parents dict
            if (previous_depth + 1) not in depths:
                depths[previous_depth + 1] = [parent]
            else:
                # otherwise, if the current parent's depth is already in the parents dict,
                # append parent to the end of the list at the current depth in the parents dict
                depths[previous_depth + 1].append(parent)

            # run the assign_depths() function on the current parent
            assign_depths(parent, previous_depth + 1)
    
    # run the assign_depths() function on the starting node
    assign_depths(starting_node, 0)

    # if the starting node has no ancestors (meaning the length of depths is 0), return -1
    if len(depths) == 0:
        return -1

    # grab the node(s) with the longest path by finding the slot with
    # the largest key in the depths dict using the max() method
    longest_path = max(depths.keys())

    # in the case that there are multiple nodes with the same depth stored in
    # longest_path, return the node with the smallest value using the min() method
    return min(depths[longest_path])