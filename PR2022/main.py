def zad4_1(array):
    counter = 0
    wynik = ''
    for el in reversed(liczby):
        if el[0] == el[-1]:
            counter = counter + 1
            wynik = el
    # print([counter, wynik])
    return [str(counter), wynik]


def zad4_2(array):
    liczby = [int(el) for el in array]
    wynik1 = 0
    wynik2 = 0
    max_count1 = 0
    max_count2 = 0

    for liczba in liczby:
        czynniki = faktoryzacja(liczba)

        if len(czynniki) > max_count1:
            wynik1 = liczba
            max_count1 = len(czynniki)
        if len(list(set(czynniki))) > max_count2:
            wynik2 = liczba
            max_count2 = len(list(set(czynniki)))

    # print([wynik1, max_count1, wynik2, max_count2])
    return [str(wynik1), str(max_count1), str(wynik2), str(max_count2)]


def zad4_3(array):
    liczby = [int(el) for el in list(set(array))]
    trojki = [(a, b, c) for a in liczby for b in liczby for c in liczby if a < b < c and b % a == 0 and c % b == 0]
    # piatki = [(a, b, c, d, e) for a in liczby for b in liczby for c in liczby for d in liczby for e in liczby if
    #           a < b < c < d < e and b % a == 0 and c % b == 0 and d % c == 0 and e % d == 0]
    # print(trojki)
    return trojki
    # cursed


def faktoryzacja(liczba):
    czynniki = []
    dzielnik = 2
    while liczba != 1:
        while liczba % dzielnik == 0:
            liczba = liczba / dzielnik
            czynniki.append(dzielnik)
        dzielnik += 1
    return czynniki


with open('przyklad.txt') as f:
    og_liczby = f.readlines()
    liczby = [liczba.strip() for liczba in og_liczby]
    wynik1 = zad4_1(liczby)
    wynik2 = zad4_2(liczby)
    wynik3 = zad4_3(liczby)
    wynik3_clean = []

    for tp in wynik3:
        converted = ""
        for num in tp:
            converted = converted + str(num) + " "
        wynik3_clean.append(converted.strip())
    output = open('wyniki.txt', 'w')
    print(wynik3_clean)
    output.write("zad1\n")
    output.writelines(line + "\n" for line in wynik1)

    output.write("zad2\n")
    output.writelines(line + "\n" for line in wynik2)

    output.write("zad3\n")
    output.writelines(line + "\n" for line in wynik3_clean)
