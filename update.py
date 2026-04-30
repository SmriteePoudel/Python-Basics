import csv

with open("employee.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    with open("updated_salary.csv", "w", newline="") as newfile:
        writer = csv.writer(newfile)
        writer.writerow(["Name", "Updated Salary"])

        for row in reader:
            name = row[0]
            salary = float(row[1])

            new_salary = salary + (salary * 0.10)

            writer.writerow([name, round(new_salary, 2)])