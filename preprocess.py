import numpy as np

def preprocessing(sepal_length, sepal_width, petal_length, petal_width):
    test_data = [
        sepal_length, 
        sepal_width, 
        petal_length, 
        petal_width
    ]

    test_data = np.array(test_data)
    test_data = test_data.reshape(1, -1)

    return test_data
