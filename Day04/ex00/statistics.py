from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculates mean, median, quartile, std, and var based on kwargs requests.
    """

    if not args:
        for _ in kwargs:
            print("ERROR")
        return

    try:
        data = sorted([float(x) for x in args])
    except (ValueError, TypeError):
        # If args contain non-numbers
        for _ in kwargs:
            print("ERROR")
        return

    n = len(data)

    mean_val = sum(data) / n

    # Population Variance formula: sum((x - mean)^2) / n
    variance_val = sum((x - mean_val) ** 2 for x in data) / n

    std_val = variance_val ** 0.5

    for key, instruction in kwargs.items():

        if instruction == "mean":
            print(f"mean : {mean_val}")

        elif instruction == "median":
            # If odd: middle element. If even: average of two middle elements.
            mid = n // 2
            if n % 2 == 1:
                median_val = data[mid]
            else:
                median_val = (data[mid - 1] + data[mid]) / 2
            print(f"median : {median_val}")

        elif instruction == "quartile":
            # 25% (Q1) and 75% (Q3)
            q1_index = int(float(n) * 0.25)
            q3_index = int(float(n) * 0.75)
            print(f"quartile : [{data[q1_index]}, {data[q3_index]}]")

        elif instruction == "std":
            print(f"std : {std_val}")

        elif instruction == "var":
            print(f"var : {variance_val}")
