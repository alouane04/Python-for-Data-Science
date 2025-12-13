import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character string."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A Student dataclass handling automatic login and ID generation."""

    name: str
    surname: str
    active: bool = True

    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Called automatically after __init__.
        We use this to construct the login based on name and surname.
        """

        self.login = self.name[0].capitalize() + self.surname.lower()
