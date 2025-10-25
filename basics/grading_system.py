def calculate_grade(avg_score):
    if avg_score >= 80:
        return "A"
    elif avg_score >= 70:
        return "B"
    elif avg_score >= 60:
        return "C"
    elif avg_score >= 50:
        return "D"
    else:
        return "F"

students_data = []

num_students = int(input("Enter number of students: "))

for i in range(num_students):
    print(f"\n--- Student {i+1} ---")
    name = input("Enter student name: ").strip()

    scores = []
    num_subjects = int(input("How many subjects? "))

    for j in range(num_subjects):
        score = float(input(f"Enter score for subject {j+1}: "))
        scores.append(score)

    avg_score = sum(scores) / len(scores)
    grade = calculate_grade(avg_score)

    students_data.append({
        "name": name,
        "average": avg_score,
        "grade": grade
    })

print("\n===== Student Grade Report =====")
for student in students_data:
    print(f"{student['name']} - Average: {student['average']:.2f} | Grade: {student['grade']}")
