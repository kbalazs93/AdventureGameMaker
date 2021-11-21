from AdventureMaker import Game, Room

welcome_text = """
Ma reggel a mezőn sétálgattál, mivel George bácsi megkért, hogy hozz neki egy kosár szedret az Északi Erdőből.
Az idő kellemes nyárutói, lágy szellő fújdogál. 
Egész tüdővel belélegzed a friss nyári illatokat és lassan körülnézel a mezőn. Bár élvezed a jó időt és a friss levegőt,
gondolatben örülnél, ha valami váratlan, rendkívüli dolog kicsit felforgatná az unalmas hétköznapokat.
"""

summer_field_description = """ A falu széléről a mezőt zöld, zsenge fű borítja, sokáig, amíg csak a szem ellát. A járást barnán előtűnő nyári utak metszik,
melyeken kilómétereken keresztül bejárható a környék.
A mező északi részén az Északi erdő fái lengetik lombjaikat, lassanként sűrűsödve határolják el magukat a falu ismerős környékétől.
Kelet felé járva a Kis Patak vize öntözi a földeket, melyek bő termést biztosítanak a falu számára.
Merre vigyen tovább az utad? """

summer_field = Room("Mező a faluhatárban", summer_field_description)


def create_game():
    return Game(welcome_text, summer_field)



