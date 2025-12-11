import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """function that takes as parameters a 2D array, prints its shape,
        and returns a truncated version of the array based on the
        provided start and end arguments"""
    try:

        assert family or isinstance(family, list) or isinstance(start, int) \
            or isinstance(end, int), "the arguments are bad"

        all_lenghts = {len(array) for array in family}

        assert len(all_lenghts) == 1, "diffrent array sizes"

        np_family = np.array(family)

        print("My shape is :", np_family.shape)

        new_family = np_family[start:end].copy()

        print("My new shape is :", new_family.shape)

        return new_family.tolist()

        # assert all( for array in family), "the arguments are bad"

    except Exception as e:
        print(e)
        return list()
