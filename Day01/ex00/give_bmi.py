import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    The function `give_bmi` calculates the Body Mass Index (BMI) based \
    on given heights and weights.
    """

    try:

        assert len(height) == len(weight), "diffrent array sizes"

        assert all(isinstance(elem, (int, float))
                   for elem in height), "the arguments are bad"
        assert all(isinstance(elem, (int, float))
                   for elem in weight), "the arguments are bad"

        np_height = np.array(height)
        np_weight = np.array(weight)

        # bmi = weight / (height ** 2)
        bmi = np_weight / (np_height * np_height)

        return bmi.tolist()

    except Exception as e:
        print(e)

# print(give_bmi([1,2,3], [2,3,4]))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    The function `apply_limit` takes a list of BMI values and a limit,
    and returns a list of boolean values indicating whether each BMI
    value exceeds the limit.
    """

    try:

        assert all(isinstance(elem, (int, float))
                   for elem in bmi), "the arguments are bad"
        assert isinstance(limit, int), "the arguments are bad"

        np_bmi = np.array(bmi)

        bool_list = np_bmi > limit

        return bool_list.tolist()

    except Exception as e:
        print(e)
