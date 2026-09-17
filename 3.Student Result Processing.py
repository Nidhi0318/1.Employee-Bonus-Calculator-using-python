total = 0
failed = False
for i in range(1, 6):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total += marks
    if marks < 35:
        failed = True
percentage = total / 5
if failed:
    grade = "F"
elif percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
print("\n--- Student Result ---")
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
if failed:
    print("Result: FAIL")
else:
    print("Result: PASS")