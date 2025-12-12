from S1E9 import Character


class Baratheon(Character):
    """Representation of a Baratheon family member with default traits."""
    def __init__(self, first_name, is_alive=True):
        """Set up a Baratheon with default appearance and life status."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Readable vector-style description of this Baratheon's traits."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Debug representation reusing the readable string form."""
        return self.__str__()


class Lannister(Character):
    """Representation of a Lannister family member with default traits."""
    def __init__(self, first_name, is_alive=True):
        """Set up a Lannister with default appearance and life status."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Readable vector-style description of this Lannister's traits."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Debug representation reusing the readable string form."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Convenience constructor to build a Lannister instance."""
        return cls(first_name, is_alive)
