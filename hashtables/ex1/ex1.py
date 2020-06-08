def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    """
    picked_weight & pairing_weight
    picked_weight is key
    pairing_weight = limit - picked_weight
    if picked_weight is biger, put it at zeroth index.
    else put it at first index.
    """
    pairing_weights = dict()

    for index in range(length):

        weight = weights[index]

        if weight in pairing_weights:

            previously_pairing_weight_index = pairing_weights[weight]

            return(index, previously_pairing_weight_index)

        pairing_weights[limit-weight] = index







    return None
