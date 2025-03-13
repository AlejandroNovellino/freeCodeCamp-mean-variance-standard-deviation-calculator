import numpy as np

def calculate(list: 'list[float]'):
    """
    Calculates the mean, the variance, standard deviation,
    max, min and sum of the list in the different axis 
    when transformed to a 3x3 numpy matrix.

    Args:
        list: ('list[float]'): list of floats to calculate the values
    
    Return
        Return a dictionary with the mean, the variance, standard deviation,
        max, min and sum of the list in the different axis 
        when transformed to a 3x3 numpy matrix.

        The form of the element is:

        {
            'mean': [axis1, axis2, flattened],
            'variance': [axis1, axis2, flattened],
            'standard deviation': [axis1, axis2, flattened],
            'max': [axis1, axis2, flattened],
            'min': [axis1, axis2, flattened],
            'sum': [axis1, axis2, flattened]
        }

    Raise
        ValueError: if the list has less than 9 values
    """

    # if length less than 9 raise a ValueError exception
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    # convert the list to a numpy matrix
    matrix = np.array(list).reshape(3, 3)

    calculations = {}

    # calculate the means
    calculations['mean'] = [
        # columns means
        np.mean(matrix, axis=0).tolist(),
        # rows means
        np.mean(matrix, axis=1).tolist(),
        # the total mean
        np.mean(matrix.flatten()).tolist()
    ]

    # calculate the variance
    calculations['variance'] = [
        # columns means
        np.var(matrix, axis=0).tolist(),
        # rows means
        np.var(matrix, axis=1).tolist(),
        # the total mean
        np.var(matrix.flatten()).tolist()
    ]

    # calculate the standard deviation
    calculations['standard deviation'] = [
        # columns means
        np.std(matrix, axis=0).tolist(),
        # rows means
        np.std(matrix, axis=1).tolist(),
        # the total mean
        np.std(matrix.flatten()).tolist()
    ]

    # calculate the max element
    calculations['max'] = [
        # columns means
        np.max(matrix, axis=0).tolist(),
        # rows means
        np.max(matrix, axis=1).tolist(),
        # the total mean
        np.max(matrix.flatten())
    ]

    # calculate the max element
    calculations['min'] = [
        # columns means
        np.min(matrix, axis=0).tolist(),
        # rows means
        np.min(matrix, axis=1).tolist(),
        # the total mean
        np.min(matrix.flatten())
    ]

    # calculate the sum
    calculations['sum'] = [
        # columns means
        np.sum(matrix, axis=0).tolist(),
        # rows means
        np.sum(matrix, axis=1).tolist(),
        # the total mean
        np.sum(matrix.flatten())
    ]

    return calculations