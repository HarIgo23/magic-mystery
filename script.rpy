# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define deathEndingFlag = False


# The game starts here.

label start:
    default findGlasses = False

    call ch1ep1 from ch1ep1Start
    if deathEndingFlag:
        return

    call ch1ep2 from ch1ep2Start
    if deathEndingFlag:
        return

    call ch1ep3 from ch1ep3Start
    if deathEndingFlag:
        return

    call ch1ep4 from ch1ep4Start
    if deathEndingFlag:
        return

    call ch1ep5 from ch1ep5Start
    if deathEndingFlag:
        return

    call ch2ep1 from ch2ep1Start
    if deathEndingFlag:
        return

    call ch2ep2 from ch2ep2Start
    if deathEndingFlag:
        return

    call ch2ep3 from ch2ep3Start
    if deathEndingFlag:
        return

    call ch2ep4 from ch2ep4Start
    if deathEndingFlag:
        return

    call ch2ep5 from ch2ep5Start
    if deathEndingFlag:
        return

    call ch3ep1 from ch3ep1Start
    if deathEndingFlag:
        return

    call ch3ep2 from ch3ep2Start
    if deathEndingFlag:
        return

    call ch3ep3 from ch3ep3Start
    if deathEndingFlag:
        return

    return
