def earliest_ancestor(ancestors, starting_node):
    # create two new dicts to store the child-parent pairs and the nodes' depths
    parents = dict()
    depths = dict()

    # for each tuple in the ancestors array, deconstruct the key-value pair
    # into parent & child nodes, then store them in the parents dict
    for key_value in ancestors:
        parent, child = key_value

        # if child's not already in the parents dict,
        # add the parent at the child in the parents dict
        if child not in parents:
            parents[child] = [parent]
        else:
            # otherwise, if child's already in the parents dict,
            # append the parent to the end of the list at the child in the parents dict
            parents[child].append(parent)

        # if parent's not already in the parents dict,
        # add an empty list at the parent in the parents dict
        if parent not in parents:
            parents[parent] = []

    # this function assigns a depth for each ancestral node
    def set_depths(starting_node, previous_depth):
        # for each parent at the starting node in the parents dict...
        for parent in parents[starting_node]:
            
            # if the parent's depth is not already in the depths dict,
            # add the parent at the current depth in the parents dict
            if (previous_depth + 1) not in depths:
                depths[previous_depth + 1] = [parent]
            else:
                # otherwise, if the parent's depth is already in the parents dict,
                # append parent to the end of the list at the current depth in parents dict
                depths[previous_depth + 1].append(parent)

            # run the set_depths() function on the parent
            set_depths(parent, previous_depth + 1)
    
    # run the set_depths() function on the starting node
    set_depths(starting_node, 0)

    # if the starting node has no ancestors (meaning the length of depths is 0), return -1
    if len(depths) == 0:
        return -1

    # grab the node(s) w/ the longest path by finding the slot w/ the largest key in depths
    longest_path = max(depths.keys())

    # if there are multiple nodes with the same depth stored in longest_path,
    # return the node with the smallest value using the min() method
    return min(depths[longest_path])