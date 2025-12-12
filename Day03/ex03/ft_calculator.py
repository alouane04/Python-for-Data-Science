class calculator:
    """Very small calculator wrapper expected to handle vector operations."""

    def __init__(self, data):
        """Store an internal list of numeric values."""
        self.data = data

    def __add__(self, object) -> None:
        """Add a scalar to the internal vector."""
        self.data = [num + object for num in self.data]
        print(self.data)

    def __mul__(self, object) -> None:
        """Multiply the internal vector by a scalar."""
        self.data = [num * object for num in self.data]
        print(self.data)

    def __sub__(self, object) -> None:
        """Subtract a scalar from the internal vector."""
        self.data = [num - object for num in self.data]
        print(self.data)

    def __truediv__(self, object) -> None:
        """Divide the internal vector by a scalar."""
        if object == 0:
            print("Error: Can't devide by 0")
        self.data = [num / object for num in self.data]
        print(self.data)
