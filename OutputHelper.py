import math

def format(informations):
    print(f"Cuvinte = {informations[0]}")
    print(f"Propozitii = {informations[1]}")

    if len(informations[2]) == 0:
        print(f"CNP(uri) = {len(informations[2])}")
    else:
        print(f"CNP(uri) = {len(informations[2])} {informations[2]}")

    if len(informations[3]) == 0:
        print(f"Telefoane = {len(informations[3])}")
    else:
        print(f"Telefoane = {len(informations[3])} {informations[3]}")

    if len(informations[4]) > 0:
        print("Litere:")
        for k,v in sorted(informations[4].items()): print(f"  {k} = {v} ({math.trunc(v * 100 / informations[5] * (10.0 ** 3)) / 10.0 ** 3}%)")

    #return informations