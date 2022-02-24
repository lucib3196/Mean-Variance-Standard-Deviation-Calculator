import numpy as np
from numpy.core.fromnumeric import mean
from numpy.matrixlib.defmatrix import mat

# Create a function named `calculate()` in `mean_var_std.py` that uses Numpy to output
# the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

def calculate(list):
    if len(list) != 9:
        raise  ValueError("List must contain nine numbers." )

    # Converts the List into a 3x3 Matrix
    array_list = np.array(list)
    matrix = array_list.reshape(3,3)

    # Empty Dictionary to store the calculations
    calculate_dic = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []}

    # The following calculations follow the same procedure 
    # Finds the given calculations for axis0, axis1 and the whole matrix
    # Convert the array into a list 
    # Append the list to the dictionary
    # Theres probably a faster way to do go through the process but this code works 


    mean1 = matrix.mean(axis=0)
    mean2 = matrix.mean(axis=1)
    mean_flattened = matrix.mean()
    calculate_dic['mean'].append(mean1.tolist())
    calculate_dic['mean'].append(mean2.tolist())
    calculate_dic['mean'].append(mean_flattened.tolist())

    varience1 = matrix.var(axis=0)
    varience2 = matrix.var(axis=1)
    varience_flattened = matrix.var()
    calculate_dic['variance'].append(varience1.tolist())
    calculate_dic['variance'].append(varience2.tolist())
    calculate_dic['variance'].append(varience_flattened.tolist())
    
    std1 = matrix.std(axis=0)
    std2 = matrix.std(axis=1)
    std_flattened = matrix.std()
    calculate_dic['standard deviation'].append(std1.tolist())
    calculate_dic['standard deviation'].append(std2.tolist())
    calculate_dic['standard deviation'].append(std_flattened.tolist())

    max1 = matrix.max(axis=0)
    max2 = matrix.max(axis=1)
    max_flattened = matrix.max()
    calculate_dic['max'].append(max1.tolist())
    calculate_dic['max'].append(max2.tolist())
    calculate_dic['max'].append(max_flattened.tolist())

    min1 = matrix.min(axis=0)
    min2 = matrix.min(axis=1)
    min_flattened = matrix.min()
    calculate_dic['min'].append(min1.tolist())
    calculate_dic['min'].append(min2.tolist())
    calculate_dic['min'].append(min_flattened.tolist())

    sum1 = matrix.sum(axis=0)
    sum2 = matrix.sum(axis=1)
    sum_flattened = matrix.sum()
    calculate_dic['sum'].append(sum1.tolist())
    calculate_dic['sum'].append(sum2.tolist())
    calculate_dic['sum'].append(sum_flattened.tolist())


    return calculate_dic


print(calculate([0,1,3,4,5,6,7,8,9]))