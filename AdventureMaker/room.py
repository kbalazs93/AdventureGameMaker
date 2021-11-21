class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def Enter(self):
        print(self.name)
        print("==========================")
        print(self.description)

