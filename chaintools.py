class Cleric:

    def __init__(self, name, position=None) -> None:
        self._name = name
        self._position = position

    def set_position(self, position) -> None:
        self._position = position

    def __str__(self) -> str:
        return f"{self._position} - {self._name}"