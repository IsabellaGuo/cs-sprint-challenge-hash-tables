def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
   
    pairing_weights = dict()

    for index in range(length):

        weight = weights[index]

        if weight in pairing_weights:

            previously_pairing_weight_index = pairing_weights[weight]

            return(index, previously_pairing_weight_index)

        pairing_weights[limit-weight] = index







    return None
