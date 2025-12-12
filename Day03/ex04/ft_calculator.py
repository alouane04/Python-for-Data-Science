class calculator:
    """Simple calculator for basic vector operations with print outputs."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Print the dot product of two equally sized numeric vectors."""
        res = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Print the element-wise sum of two numeric vectors."""
        res = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Print the element-wise subtraction of vector V2 from V1."""
        res = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
