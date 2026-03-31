# 7. Készíts egy függvényt `calculate_average`, névvel, amely paraméterként egy számokat tartalmazó listát kap,
# és visszaadja számok átlagát!

# Készíts egy másik függvényt is `calculate_class_average` névvel, amely paraméterként egy olyan listát kap, ami tuple-öket tartalmaz.
# A tuple-öknek két eleme van az egyik egy tanuló neve, a másik pedig egy érdemjegy.

# pl.: `students = [("John", 5), ("Jane", 2), ("Mark", 3), ("Sarah", 4)]`
# Ez a függvény adja vissza, hogy a teljes osztálynak (list összes eleme) mennyi az átlaga.
# Ezen a függvényen belül kell meghívnod a `calculate_average` függvényt!

students = [("John", 5), ("Jane", 2), ("Mark", 3), ("Sarah", 4)]
print(students[0][1])


def calculate_average(numbers):
    # summa = 0
    # for number in numbers:
    #     summa += number
    # return summa / len(numbers)
    return sum(numbers) / len(numbers)


def calculate_class_average(students):
    # grades = []
    # for _, grade in students:
    #     grades.append(grade)
    # return calculate_average(grades)

    grades = [grade for _, grade in students]
    return calculate_average(grades)


print(calculate_class_average(students))
