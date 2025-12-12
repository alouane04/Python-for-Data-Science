from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base for GoT characters with a name and life status."""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initialize a character with a first name and alive flag."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Mark the character as dead."""
        self.is_alive = False


class Stark(Character):
    """House Stark member; inherits common character behavior."""
    def __init__(self, first_name, is_alive=True):
        """Create a Stark with optional alive status (defaults to alive)."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Mark this Stark as dead (keeps Character.die behavior)."""
        super().die()
