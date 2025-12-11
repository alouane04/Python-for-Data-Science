from numpy.typing import NDArray
from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """A program that should load the image "animal.jpeg",
        print some information
        about it and display it after "zooming"""

    try:
        path = "animal.jpeg"

        np_image: NDArray = ft_load(path)

        print(np_image)

        # Slice
        zoomed_img = np_image[100:500, 450:850]

        # Gray it
        r = zoomed_img[:, :, 0].astype(int)
        g = zoomed_img[:, :, 1].astype(int)
        b = zoomed_img[:, :, 2].astype(int)

        grayscale = (r + g + b) / 3.0

        grayscale = grayscale.astype(int)

        # Rechape it
        final_img = grayscale.reshape(
            (grayscale.shape[0], grayscale.shape[1], 1)
        )

        print("New shape after slicing:", final_img.shape)
        print(final_img)

        plt.imshow(final_img, cmap="gray")
        plt.show()

    except FileNotFoundError:
        print("Error: The file was not found.")
        return None

    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    main()
