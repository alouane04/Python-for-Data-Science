import array
import imageio.v2 as iio
from numpy.typing import NDArray


def ft_load(path: str) -> array:
    """ function that loads an image, prints its format, and its pixels
    content in RGB format"""
    try:

        assert path and isinstance(path, str) and \
            path.lower().endswith((".jpg", ".jpeg")), "Error: Path Problem"

        np_image: NDArray = iio.imread(path)

        print("The shape of image is:", np_image.shape)

        return np_image

    except FileNotFoundError:
        print("Error: The file was not found.")
        return None

    except Exception as e:
        print("Error:", e)
        return None
