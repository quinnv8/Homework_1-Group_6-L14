import os

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def l1(u, v):
    """Computes the L1 distance between two vectors.

    Args:
        u: A 1-dimensional np.array object
        v: A 1-dimensional np.array object

    Returns:
        The L1 distance between u and v
    """

    return sum(abs(u - v))


def load_data(filename):
    """Loads the data into a np array, where each row corresponds to an image patch.

    Args:
        filename: The path to the data file

    Returns:
        A np array, where each row corresponds to an image patch
    """

    return np.genfromtxt(filename, delimiter=',')


def create_function(dimensions, thresholds):
    """Creates a hash function from a list of dimensions and thresholds.

    Args:
        dimensions: A list of dimensions
        thresholds: A list of thresholds

    Returns:
        A hash function

    Example:
        >>> dimensions = [0, 3, 4]
        >>> thresholds = [10, 20, 30]
        >>> f = create_function(dimensions, thresholds)
        >>> f(np.array([1, 12, 3, 40, 50]))
        '011'
    """

    def f(v):
        """Hash function.

        Args:
            v: A 1-dimensional np.array object

        Returns:
            A string of 0s and 1s
        """

        boolarray = [v[dimensions[i]] >= thresholds[i]
                     for i in range(len(dimensions))]
        return "".join(map(str, map(int, boolarray)))

    return f


def create_functions(k, L, num_dimensions=400, min_threshold=0, max_threshold=255):
    """Creates the LSH functions (functions that compute L K-bit hash keys).

    Args:
        k: The number of dimensions to select at random
        L: The number of hash functions to create
        num_dimensions: The number of dimensions in the data
        min_threshold: The minimum threshold to use
        max_threshold: The maximum threshold to use

    Returns:
        A list of L hash functions
    """

    functions = []
    for i in range(L):
        dimensions = np.random.randint(low=0,
                                       high=num_dimensions,
                                       size=k)
        thresholds = np.random.randint(low=min_threshold,
                                       high=max_threshold + 1,
                                       size=k)

        functions.append(create_function(dimensions, thresholds))

    return functions


def hash_vector(functions, v):
    """Hashes a vector using a list of hash functions.

    Args:
        functions: A list of hash functions
        v: A 1-dimensional np.array object

    Returns:
        A list of L K-bit hash keys
    """

    return np.array([f(v) for f in functions])


def hash_data(functions, A):
    """Hashes a dataset of vectors using a list of hash functions.

    Args:
        functions: A list of hash functions
        A: A 2-dimensional np.array object, where each row is a vector

    Returns:
        A 2-dimensional np.array object, where each row is a list of L K-bit hash keys
    """

    return np.array(list(map(lambda v: hash_vector(functions, v), A)))


def get_candidates(hashed_A, hashed_point, query_index):
    """Finds the candidates for a given query point. 
    A candidate is a point that has the same hash key as the query point. 

    Args:
        hashed_A: A 2-dimensional np.array object, where each row is a list of L K-bit hash keys
        hashed_point: A list of L K-bit hash keys
        query_index: The index of the query point in the dataset

    Returns:
        A list of indices of candidate points
    """

    return filter(lambda i: i != query_index and
                  any(hashed_point == hashed_A[i]), range(len(hashed_A)))


def lsh_setup(A, k=24, L=10):
    """Runs the LSH setup algorithm. 

    Args:
        A: A 2-dimensional np.array object, where each row is a vector
        k: The number of dimensions to select at random
        L: The number of hash functions to create

    Returns:
        A tuple of (functions, hashed_A), where functions is a list of L hash functions 
        and hashed_A is a 2-dimensional np.array object, where each row is a list of L K-bit hash keys
    """

    functions = create_functions(k=k, L=L)
    hashed_A = hash_data(functions, A)
    return (functions, hashed_A)


def lsh_search(A, hashed_A, functions, query_index, num_neighbors=10):
    """Runs the LSH search algorithm. 

    Args:
        A: A 2-dimensional np.array object, where each row is a vector
        hashed_A: A 2-dimensional np.array object, where each row is a list of L K-bit hash keys
        functions: A list of hash functions
        query_index: The index of the query point in the dataset
        num_neighbors: The number of neighbors to return

    Returns:
        A list of indices of the nearest neighbors
    """

    # Compute the hash key for the query point
    hashed_point = hash_vector(functions, A[query_index, :])

    # Find the candidates that have the same hash key as the query point
    candidate_row_nums = get_candidates(hashed_A, hashed_point, query_index)

    # Compute the distances to the candidates
    distances = map(lambda r: (
        r, l1(A[r], A[query_index])), candidate_row_nums)

    # Sort the candidates by distance and return the indices of the nearest neighbors
    best_neighbors = sorted(distances, key=lambda t: t[1])[:num_neighbors]

    return [t[0] for t in best_neighbors]


def plot(A, row_nums, base_filename, output_path=None, grid_size=None, title=None):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    patch_list = []
    # Loop over each row number
    for row_num in row_nums:
        # Reshape the row into a 20x20 image
        patch = np.reshape(A[row_num, :], [20, 20])
        patch_list.append(patch)
        # Save the image
        im = Image.fromarray(patch)
        if im.mode != 'RGB':
            im = im.convert('RGB')
        path = ""
        if output_path is not None:
            path = os.path.join(output_path, f"{base_filename}_{row_num}.png")
        else:
            path = f"{base_filename}_{row_num}.png"

        im.save(path)

    if grid_size is not None:
        # Create a grid of images
        fig, ax = plt.subplots(grid_size[0], grid_size[1], figsize=(
            10, 6), constrained_layout=True)
        if title is not None:
            fig.suptitle(title)
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                ax[i, j].imshow(patch_list[i * grid_size[1] + j], cmap='gray')
                ax[i, j].axis('off')
                ax[i, j].set_title(f"Image {row_nums[i * grid_size[1] + j]}")
    else:
        for i in range(len(row_nums)):
            plt.imshow(patch_list[i], cmap='gray')
            plt.axis('off')
            plt.title(f"Image {row_nums[i]}")

    plt.show()


def linear_search(A, query_index, num_neighbors):
    """Runs the linear search algorithm. 

    Args:
        A: A 2-dimensional np.array object, where each row is a vector
        query_index: The index of the query point in the dataset
        num_neighbors: The number of neighbors to return

    Returns:
        A list of indices of the nearest neighbors
    """

    # Compute the distances to all points
    distances = map(lambda r: (
        r, l1(A[r], A[query_index])), range(len(A)))

    # Filter out the query point
    distances = filter(lambda t: t[0] != query_index, distances)

    # Sort the candidates by distance and return the indices of the nearest neighbors
    best_neighbors = sorted(distances, key=lambda t: t[1])[:num_neighbors]

    return [t[0] for t in best_neighbors]


def error_measure(A, query_index, linear_neighbors, lsh_neighbors):
    """Computes the error measure for the given query point.

    Args:
        A: A 2-dimensional np.array object, where each row is a vector
        query_index: The index of the query point in the dataset
        linear_neighbors: A list of indices of the nearest neighbors returned by the linear search algorithm
        lsh_neighbors: A list of indices of the nearest neighbors returned by the LSH algorithm

    Returns:
        The error measure
    """

    # Compute the distances to the nearest neighbors
    linear_distances = list(
        map(lambda r: l1(A[r], A[query_index]), linear_neighbors))
    lsh_distances = list(
        map(lambda r: l1(A[r], A[query_index]), lsh_neighbors))

    # Compute the error measure
    linear_error = np.sum(linear_distances)
    lsh_error = np.sum(lsh_distances)

    return lsh_error / linear_error
