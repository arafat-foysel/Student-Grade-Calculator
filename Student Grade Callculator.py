subjects = ["Bangla", "English", "Math", "Science", "General Knowledge"]
marks = []

for subject in subjects:
    obtain_marks = float(input(f"Enter marks for {subject}: "))
    marks.append(obtain_marks)

total_marks = sum(marks)
print("your obtained total marks: ", total_marks)

average_marks = total_marks / len(subjects)
print("your obtained average marks: ", round(average_marks, 2))

if average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
print("\n--- Result ---")
