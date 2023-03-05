from AdventureMaker import Room

georges_house_description = """ Ahogy visszatérsz a mezőről, megpillantod George házát. A fújdogáló szél hajlitgassa a ház ágait.
 George a ház előtt nézegeti a virágait. Arra gondolsz, hogy milyen mérges lenne, hogyha üres kézzel mennél haza. 
 Elnézve révedező tekintetét talán bölcsebb lenne, hogyha visszamennél oda, ahonnan jöttél."""

directions = ["mez"]

georges_house = Room("George bácsi háza", georges_house_description, directions=directions)