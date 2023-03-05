from AdventureMaker import Room

summer_field_description = """ A falu széléről a mezőt zöld, zsenge fű borítja, sokáig, amíg csak a szem ellát. A járást barnán előtűnő nyári utak metszik,
melyeken kilómétereken keresztül bejárható a környék.
A mező északi részén az Északi erdő fái lengetik lombjaikat, lassanként sűrűsödve határolják el magukat a falu ismerős környékétől.
Kelet felé járva a Kis Patak vize öntözi a földeket, melyek bő termést biztosítanak a falu számára.
Merre vigyen tovább az utad? """

directions = ["patak"]

summer_field = Room("Mező a faluhatárban", summer_field_description, directions=directions)
