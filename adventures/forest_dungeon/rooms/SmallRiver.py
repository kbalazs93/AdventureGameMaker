from AdventureMaker import Room

small_river_description = """ Elérkeztél a kis patak partjára, ahol a víz lassú folyással csordogál. A patakot nádas szegélyezi,
ám egy kis részen le tudsz jutni a partjára. Ha szeretnél, meríthetsz vizet a patakból, vagy mehetsz tovább északra az erdőbe.
"""

directions = ["mez", "erd"]

small_river = Room("Kis patak", small_river_description, directions=directions)
