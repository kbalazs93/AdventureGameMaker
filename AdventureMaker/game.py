
class Game(object):

    def __init__(self, welcome_text, starting_room):
        self.welcome_text = welcome_text
        self.starting_room = starting_room

    def start(self):
        print(self.welcome_text)
        self.starting_room.Enter()
        answer = input(" > ")
        print(answer)



