import os


def clear():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def header():
    print("******************************************************")
    print("\t\tEm um dia, que série melhor\n\t\t representa você")
    print("******************************************************")
