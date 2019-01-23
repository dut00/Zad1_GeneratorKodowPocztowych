# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

kod1 = "79-900"
kod2 = "80-155"


def GenerujKodyPocztowe(kp1, kp2):
    # dzieli stringa i zamienia na inty
    [a1, a2] = [int(x) for x in kp1.split('-')]
    [b1, b2] = [int(x) for x in kp2.split('-')]

    # szereguje kody rosnąco
    if (a1 == b1):
        if (a2 > b2):
            [a2, b2] = [b2, a2]
    elif (a1 > b1):
        [a1, a2, b1, b2] = [b1, b2, a1, a2]

    # pomija pierwszy kod - wypisuje tylko te pomiedzy
    a2 += 1

    # wypisuje kody w kolejnoci rosnącej
    if (a1 == b1):
        for i in range(a2, b2):
            print(f"{a1:02}-{i:03}")

    else:  # if (a1 < b1):
        for i in range(a2, 1000):
            print(f"{a1:02}-{i:03}")

        a1 += 1

        while (a1 < b1):
            for i in range(0, 1000):
                print(f"{a1:02}-{i:03}")
            a1 += 1

        for i in range(0, b2):
            print(f"{a1:02}-{i:03}")


GenerujKodyPocztowe(kod1, kod2)
