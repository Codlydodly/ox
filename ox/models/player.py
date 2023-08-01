from uuid import UUID
from dataclasses import dataclass


@dataclass
class Player:
    id: UUID
    display_name: str

    def __eq__(self, other):
        if type(other) is Player:
            if other.id == self.id:
                return True
        return False
