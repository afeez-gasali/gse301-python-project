# ================================================================
# Student Academic Performance Analysis System
# GSE301 = Data Science (Python Fundamentals) 
# ================================================================


# ------------- Part 1: Data Collection & Storage ----------------

# Task 1.1: Variable Declaration
student_name = "Rasheed Fatia"
matric_number = "23/60AC389"
age = 21
cgpa = 4.81
is_active = True
courses_registered = ["Python", "Statistics", "Data Science"]
grades = {
    "Python" : "A",
    "Statistics" : "A",
    "Data Science" : "A"
}


# Task 1.2: Data Structures
department_info = ("Religion Department", "Faculty of Technology", 2025)

students = [
    {
        "name": "Rasheed Fatia",
        "matric" : "23/60AC389",
        "age" : 21,
        "cgpa": 4.81,
        "active": True,
        "courses": [
            "Python",
            "Statistics",
            "Data Science"
        ],
        "outstanding": 0
    },
    {
        "name": "Yusuf Adeoye",
        "matric" : "23/70JC093",
        "age" : 22,
        "cgpa": 3.45,
        "active": True,
        "courses": [
            "Python",
            "Algorithms",
        ],
        "outstanding": 0
    },
    {
        "name": "Moses Oyedele",
        "matric" : "23/10EE102",
        "age" : 24,
        "cgpa": 2.80,
        "active": True,
        "courses": [
            "Networking",
            "Python",
        ],
        "outstanding": 1
    },
    {
        "name": "Timi Abioye",
        "matric" : "23/22ME211",
        "age" : 20,
        "cgpa": 3.90,
        "active": True,
        "courses": [
            "Python",
            "Statistics",
        ],
        "outstanding": 0
    },
    {
        "name": "Nimah Nina",
        "matric" : "23/90DS019",
        "age" : 19,
        "cgpa": 4.20,
        "active": False,
        "courses": [
            "Python",
            "Data Science"
        ],
        "outstanding": 0
    },
]

student_names = [students[0] for student in students]
unique_courses = set(course for s in students for course in s["courses"])


# ---------------- Part 2: Data Processing & Logic ----------------------

# Task 2.1: Grading Function

def grade_score(score: int) -> str:
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"

    
    match grade:
        case "A":
            print("Excellent performance")
        case "B":
            print("Very good.")
        case "C":
            print("Good effort.")
        case "D":
            print("Fair result.")
        case "E":
            print("Needs improvement.")
        case "F":
            print("Failed.")
    
    return grade


# Task 2.2: Type Conversion & Validation & C:/Python311/python.exe

def validate_user_input():
    try:
        age_input = int(input("Enter age: "))
        cgpa_input =  float(input("Enter CGPA: "))

        if not(16 <= age_input <= 40):
            raise ValueError("Age must be between 16 and 40")
        
        if not (0.0 <= cgpa_input <= 5.0):
            raise ValueError("CGPA must be between 0.0 and 5.0")
        
        return age_input, cgpa_input
    except ValueError as error:
        print("Invalid input:", error)
        return None, None
    


# ------------------ Part 3: Analysis & Reporting -------------------

# Task 3.1: List Slicing
assignment_scores = [45, 78, 88, 67, 90, 56, 72, 81, 69, 95]

top_3 = assignment_scores[:3]
last_5 = assignment_scores[-5:]
every_other = assignment_scores[::2]

# Task 3.2: Set Operations

set_pass = {
    "Rasheed Fatia",
    "Yusuf Adeoye",
    "Timi Abidoye",
    "Nimah Nina"
}

set_merit = {
    "Rasheed Fatia",
    "Nimah Nina"
}

passed_and_merit = set_pass & set_merit
all_students = set_pass | set_merit
passed_no_merit = set_pass - set_merit

# --------------------------- Part 4: Interactive Menu -------------------------

def check_graduation_eligibility(student):
    if student["cgpa"] >= 2.5 and student["outstanding"] == 0 and student["active"]:
        return True, f"{student['name']} is eligible for graduation."
    else:
        return False, f"{student['name']} is NOT eligible for graduation"


def find_top_performer():
    return max(students, key=lambda x: x["cgpa"])


def display_menu():
    print("\n1. View all students")
    print("2. Add new student")
    print("3. Check eligibility for graduation")
    print("4. Find top performer")
    print("5. Exit")


while True:
    print("\n=====================================================================")
    print("Student Academic Performance System")
    print("\n=====================================================================")

    display_menu()
    choice = input("Enter your choice:")

    match choice:
        case "1":
            print("\nList of Students")
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student['name']}")
        case "2":
            name = input("Enter name: ")
            matric = input("Enter matric number: ")
            age, cgpa = validate_user_input()
            if age is None:
                continue
            active = input("Is active (yes/no): ").lower() == "yes"
            courses = input("Enter courses (comma seperated): ").split(",")
            students.append({
                "name": name,
                "matric": matric,
                "age": age,
                "cgpa": cgpa,
                "active": active,
                "courses": [c.strip() for c in courses],
                "outstanding": 0
            })
            
            print("Student added successfully.")
        case "3":
            name = input("Enter student name: ")
            found = False
            for student in students:
                if student["name"].lower() == name.lower():
                    found = True
                    status, message = check_graduation_eligibility(student)
                    print(message)
            if not found:
                print("Student not found.")
        case "4":
            top = find_top_performer()
            print("\nTop Performer")
            print(f"Matric: {top['matric']}")
            print(f"CGPA: {top['cgpa']}")
            print(f"Courses: {top['courses']}")
        case "5":
            print("Exiting the system Goodbye!")
            break
        case _:
            print("Invalid choice. Try again")
        