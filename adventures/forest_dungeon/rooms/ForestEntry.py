from AdventureMaker import Room

forest_entry_description = """ Ahogy megérkezel az erdőbe, feltűnik, nagyon sejtelmessé válik a környezet. A fák sötétséget árasztanak maguk körül. Nem érzed már a 
nyár kellemes melegét, sokkal inkább baljós előjeleket. Ha sietsz, még gyorsan elérheted a szeder bokrot, ami tőled nem messze található.
"""

directions = ["mez", "patak"]

forest_entry = Room("Az erdő bejárata", forest_entry_description, directions=directions)
