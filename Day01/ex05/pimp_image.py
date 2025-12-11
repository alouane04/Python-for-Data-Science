import array
import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    img = array.copy()

    img = 255 - array

    plt.imshow(img)
    plt.show()
    return img


def ft_red(array) -> array:
    """make the color Red of the image received."""
    img = array.copy()

    # Multiplying by a list of [1, 0, 0] broadcasts it to every pixel
    img = img * [1, 0, 0]

    plt.imshow(img)
    plt.show()
    return img


def ft_green(array) -> array:
    """make the color Green of the image received."""
    img = array.copy()

    # Subtract the Red channel from itself
    img[:, :, 0] = img[:, :, 0] - img[:, :, 0]
    # Subtract the Blue channel from itself
    img[:, :, 2] = img[:, :, 2] - img[:, :, 2]

    plt.imshow(img)
    plt.show()
    return img


def ft_blue(array) -> array:
    """make the color Blue of the image received."""
    img = array.copy()

    # Directly assign 0 to the Red
    img[:, :, 0] = 0
    # Directly assign 0 to the Red
    img[:, :, 1] = 0

    plt.imshow(img)
    plt.show()
    return img


def ft_grey(array) -> array:
    """make the color Gey of the image received."""
    img = array.copy()

    # Calc the sum cause we can't use +
    img_sum = np.sum(img, axis=2)

    # devide the sum to get the Individual
    img_sum = img_sum / 3

    # Assign the gray for each color channel
    img[:, :, 0] = img_sum
    img[:, :, 1] = img_sum
    img[:, :, 2] = img_sum

    plt.imshow(img)
    plt.show()
    return img
