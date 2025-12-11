from numpy.typing import NDArray
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """A program that should load the image "animal.jpeg",
        print some information
        about it and display it after "zooming"""

    try:
        path = "animal.jpeg"

        np_image: NDArray = ft_load(path)

        # print(np_image)

        # Slice
        zoomed_img = np_image[100:500, 450:850]

        # Gray it
        r = zoomed_img[:, :, 0].astype(int)
        g = zoomed_img[:, :, 1].astype(int)
        b = zoomed_img[:, :, 2].astype(int)

        grayscale = (r + g + b) / 3.0

        grayscale = grayscale.astype(int)

        zoom_img = grayscale.reshape(
            (grayscale.shape[0], grayscale.shape[1])
        )

        print("The shape of image is:", zoom_img.shape)

        print(zoom_img)

        # Creating a black image using a NumPy array
        transpose_img = np.zeros((zoom_img.shape[0], zoom_img.shape[1]))

        for i in range(zoom_img.shape[0]):
            for j in range(zoom_img.shape[1]):
                transpose_img[j, i] = zoom_img[i, j]

        print("New shape after Transpose:", transpose_img.shape)
        print(transpose_img)

        plt.imshow(transpose_img, cmap="gray")
        plt.show()

    except FileNotFoundError:
        print("Error: The file was not found.")
        return None

    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    main()
