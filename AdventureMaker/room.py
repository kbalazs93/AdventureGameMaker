class Room(object):

    def __init__(self, name, description, directions):
        self._name = name
        self._description = description
        self._directions = directions

    def Enter(self):
        print(self._name)
        print("==========================")
        print(self._description)

    @property
    def directions(self):
        return self._directions




