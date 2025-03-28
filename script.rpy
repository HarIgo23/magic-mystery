# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define badEndingFlag = False


# The game starts here.

label start:
    default findGlasses = False
    default wantToExit = False
    default findExit = False
    default visitedPlaces = set()

    call ch1ep1 from ch1ep1Start
    if badEndingFlag:
        return

    call ch1ep2 from ch1ep2Start
    if badEndingFlag:
        return

    call ch1ep3 from ch1ep3Start
    if badEndingFlag:
        return

    call ch2ep1 from ch2ep1Start
    if badEndingFlag:
        return

    call ch2ep2 from ch2ep2Start
    if badEndingFlag:
        return

    call ch2ep3 from ch2ep3Start
    if badEndingFlag:
        return

    call ch2ep4 from ch2ep4Start
    if badEndingFlag:
        return

    call ch2ep5 from ch2ep5Start
    if badEndingFlag:
        return

    call ch3ep1 from ch3ep1Start
    if badEndingFlag:
        return

    call ch3ep2 from ch3ep2Start
    if badEndingFlag:
        return

    call ch3ep3 from ch3ep3Start
    if badEndingFlag:
        return

    return
