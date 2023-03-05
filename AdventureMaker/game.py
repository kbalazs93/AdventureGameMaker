from AdventureMaker.Utils.HelperFunctions import KeywordProcessor


class Game(object):

    def __init__(self, welcome_text, rooms, starting_room):
        self.welcome_text = welcome_text
        self.rooms = rooms
        self.current_room = starting_room
        self.keyword_processor = KeywordProcessor()

    def start(self):
        print(self.welcome_text)
        self.rooms[self.current_room].Enter()
        while True:
            answer = input(" > ")
            if answer == "exit":
                break
            elif self.keyword_processor.isAswerInKeywordCollection(answer, self.rooms[self.current_room].directions):
                answer = self.keyword_processor.lastFoundKeyword
                self.current_room = answer
                self.rooms[answer].Enter()
            else:
                print("Sajnálom, innen ilyen helyre nem mehetsz: {}".format(answer))
        print("Köszönöm a játéok!")
