from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Hybrid heir who inherits traits from both Baratheon and Lannister."""

    def __init__(self, first_name):
        """Initialize a king with combined lineage defaults."""
        super().__init__(first_name)

    @property
    def eyes(self):
        """Current eye color for the king."""
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        """Update the king's eye color."""
        self._eyes = value

    @property
    def hairs(self):
        """Current hair color for the king."""
        return self._hairs

    @hairs.setter
    def hairs(self, value):
        """Update the king's hair color."""
        self._hairs = value

    def set_eyes(self, color):
        """Public setter for eyes to match exercise style."""
        self.eyes = color

    def set_hairs(self, color):
        """Public setter for hairs to match exercise style."""
        self.hairs = color

    def get_eyes(self):
        """Return the current eye color."""
        return self.eyes

    def get_hairs(self):
        """Return the current hair color."""
        return self.hairs
