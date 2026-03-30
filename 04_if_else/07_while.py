for i in range(6):
    print(i)


# i = 0
# while i < 6:
#     print(i)
#     i += 1

min_grade = 1
max_grade = 5
while True:
    grade = input("Enter your grade (1-5): ")
    if grade.isdigit() and min_grade <= int(grade) <= max_grade:
        print("Thank you.")
        break
    print("Invalid grade, try again.")
