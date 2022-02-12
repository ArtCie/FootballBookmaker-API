from collections.abc import Iterator


class RoundRepositoryIterator(Iterator):
    _position: int = None

    def __init__(self, _list: list) -> None:
        self._list = _list
        self._position = -1

    def __next__(self):
        try:
            value = self._list[self._position]
            self._position += 1
            return value
        except IndexError:
            raise StopIteration()
