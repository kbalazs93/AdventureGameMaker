from AdventureMaker import Game
from adventures.forest_dungeon import rooms_dict

welcome_text = """
Ma reggel a mezőn sétálgattál, mivel George bácsi megkért, hogy hozz neki egy kosár szedret az Északi Erdőből.
Az idő kellemes nyárutói, lágy szellő fújdogál. 
Egész tüdővel belélegzed a friss nyári illatokat és lassan körülnézel a mezőn. Bár élvezed a jó időt és a friss levegőt,
gondolatben örülnél, ha valami váratlan, rendkívüli dolog kicsit felforgatná az unalmas hétköznapokat.
"""


class ForestGame(Game):

    def __init__(self):
        super(ForestGame, self).__init__(welcome_text, rooms=rooms_dict, starting_room="mez")


ForestDungeon = ForestGame()
