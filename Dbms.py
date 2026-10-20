students = [
    {"student_id": 1, "full_name": "Mary Wanjiku", "email": "mary@gmail.com", "course": "Computer Science", "year": 1},
    {"student_id": 2, "full_name": "Brian Otieno", "email": "brian@gmail.com", "course": "Software Engineering", "year": 2},
    {"student_id": 3, "full_name": "Kevin Mwangi", "email": "kevin@gmail.com", "course": "Data Science", "year": 1}
]

def view_students(student_list):
    if not student_list:
        print("\nNo students found!\n")
        return
    print(f"\n--- Found {len(student_list)} student(s) ---")
    for s in student_list:
        print(f"ID: {s['student_id']} | Name: {s['full_name']} | Course: {s['course']} | Year: {s['year']} | Email: {s['email']}")
    print("-" * 60 + "\n")

def add_student():
    print("\n--- ADD NEW STUDENT ---")
    try:
        new_id = max([s["student_id"] for s in students]) + 1 if students else 1
        full_name = input("Full Name: ").strip()
        email = input("Email: ").strip()
        course = input("Course: ").strip()
        year = int(input("Year (1-4): "))

        students.append({
            "student_id": new_id,
            "full_name": full_name,
            "email": email,
            "course": course,
            "year": year
        })
        print(f"✅ Student {full_name} added successfully!\n")
    except ValueError:
        print("❌ Year must be a number!\n")

def search_by_course():
    query = input("\nEnter course to search: ").lower().strip()
    results = [s for s in students if query in s["course"].lower()]
    view_students(results)

def search_by_year():
    try:
        query = int(input("\nEnter year to search (1-4): "))
        results = [s for s in students if s["year"] == query]
        view_students(results)
    except ValueError:
        print("❌ Please enter a number!\n")

# MAIN MENU
while True:
    print("STUDENT MANAGEMENT SYSTEM")
    print("=" * 27)
    print("1. View all students")
    print("2. Add student")
    print("3. Search by course")
    print("4. Search by year")
    print("5. Exit")
    
    choice = input("Choose option (1-5): ")

    if choice == "1":
        view_students(students)
    elif choice == "2":
        add_student()
    elif choice == "3":
        search_by_course()
    elif choice == "4":
        search_by_year()
    elif choice == "5":
        print("Bye! 👋")
        break
    else:
        print("Invalid choice! Try 1-5\n")