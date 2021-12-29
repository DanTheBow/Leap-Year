print("Formel für Schaltjahre:")
print("Ist die Jahreszahl durch 4 teilbar, aber nicht durch 100, ist es ein Schaltjahr.")
print("Ist die Jahreszahl durch 100 teilbar, aber nicht durch 400, ist es kein Schaltjahr.")
print("Ist die Jahreszahl durch 400 teilbar, dann ist es ein Schaltjahr.")
print()


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print("Schaltjahr")
    elif year % 100 == 0 and year % 400 != 0:
        print("Kein Schaltjahr")
    elif year % 400 == 0:
        print("Schaltjahr")
    else:
        print("Kein Schaltjahr")


leap_year(int(input("Geben Sie bitte ein Jahr ein: ")))
