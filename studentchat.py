class Student:
    def __init__(self):
        self.name = ""
        self.usn = ""
        self.marks = []

    def get_student_details(self):
        self.name = input("Enter name: ")
        self.usn = input("Enter USN: ")
        for i in range(5):
            while True:
                try:
                    marks = int(input(f"Enter marks of subject {i+1}: "))
                    if 0 <= marks <= 100:
                        self.marks.append(marks)
                        break
                    else:
                        print("Marks should be between 0 and 100")
                except ValueError:
                    print("Invalid input! Please enter a valid integer.")

    def calculate_grade(self):
        total_marks = sum(self.marks)
        percentage = total_marks / 500 * 100
        
        print("Total marks:", total_marks)
        print("Percentage:", percentage)
        if 80 <= percentage <= 100:
            grade = "A"
        elif 60 <= percentage <= 79:
            grade = "B"
        elif 40 <= percentage <= 59:
            grade = "C"
        else:
            grade = "F"
        print("Grade:", grade)
        return grade

    def convert_to_list(self):
        return [self.usn, self.name, self.marks, self.calculate_grade()]

    def write_to_file(self, filename):
        with open(filename, "a") as file:
            data = ','.join(map(str, self.convert_to_list())) + '\n'
            file.write(data)

# Create an instance of the Student class
student = Student()

# Get student details
student.get_student_details()

# Calculate and display grade
grade = student.calculate_grade()

# Write student data to a file
student.write_to_file("studentclass.txt")
