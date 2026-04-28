# Simple Student Result System 

students = []

num = int(input("Enter number of students: "))

# Loop for each student
for i in range(num):
    print("\nStudent", i + 1)

    name = input("Enter name: ")

    # Input marks for 3 subjects
    math = float(input("Math marks: "))
    english = float(input("English marks: "))
    cs = float(input("CS marks: "))

    #  validation
    if math > 100 or english > 100 or cs > 100:
        print("Invalid marks! Skipping student.")
        continue

    total = math + english + cs
    percentage = (total / 300) * 100

    # Grade system
    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    result = "PASS" if percentage >= 40 else "FAIL"

    students.append([name, total, percentage, grade, result])

print("\n===== FINAL RESULT SHEET =====")
print("Name\tTotal\tPercentage\tGrade\tResult")

for s in students:
    print(f"{s[0]}\t{s[1]}\t{s[2]:.2f}%\t\t{s[3]}\t{s[4]}")