class Injury:
    def __init__(self, name, id_):
        self._id = id_
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name