import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    np_array = np.array(list).reshape((3, 3))
    mean = [
        np.mean(np_array, axis=0).tolist(),
        np.mean(np_array, axis=1).tolist(),
        np.mean(np_array)
    ]

    variance = [
        np.var(np_array, axis=0).tolist(),
        np.var(np_array, axis=1).tolist(),
        np.var(np_array)
    ]

    st_deviation = [
        np.std(np_array, axis=0).tolist(),
        np.std(np_array, axis=1).tolist(),
        np.std(np_array)
    ]

    np_max = [
        np.max(np_array, axis=0).tolist(),
        np.max(np_array, axis=1).tolist(),
        np.max(np_array)
    ]
    
    np_min = [
        np.min(np_array, axis=0).tolist(),
        np.min(np_array, axis=1).tolist(),
        np.min(np_array)
    ]
    
    np_sum = [
        np.sum(np_array, axis=0).tolist(),
        np.sum(np_array, axis=1).tolist(),
        np.sum(np_array)
    ]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': st_deviation,
        'max': np_max,
        'min': np_min,
        'sum': np_sum
    }

    return calculations

example = calculate([1,2,3,4,5,6,7,8,9])
print(example)

# to run it: terminal > python3 + [filename]