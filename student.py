import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    with open("passed.csv", "w", newline="") as newfile:
        writer = csv.writer(newfile)
        writer.writerow(["Name", "Marks", "Grade"])

        for row in reader:
            name = row[0]
            marks = int(row[1])

            if marks >= 80:
                grade = "A"
            elif marks >= 60:
                grade = "B"
            elif marks >= 40:
                grade = "C"
            else:
                grade = "Fail"

            if marks >= 40:
                writer.writerow([name, marks, grade])