def catandmouse(catA, catB, mouseC):

    mylist = [catA, catB, mouseC]
    for n in mylist:
        if n < 0 or n > 100:
            return "must between 0-100"

    cata = catA
    catb = catB
    mousec = mouseC

    A_C = abs(cata - mousec)
    B_C = abs(catb - mousec)

    if A_C > B_C:
        return "Cat B"
    elif A_C < B_C:
        return "Cat A"
    else:
        return "Mouse C"
