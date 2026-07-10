#Assignment1 
#Class Number B33


#Input Collection & Validation
 
students = []  # Master list that holds every student dictionary
 
while True:
    # Ask for a student name or 'done' to stop entering students
    name = input("\nEnter student name (or 'done'): ").strip()
 
    if name.lower() == "done":
        break  # Admin is finished entering students
 
    if name == "":
        print("Name cannot be empty. Please try again.")
        continue  # Skip back to the top of the loop
 
 
    # Collect exactly 3 validated scores for this student
    scores = []
    for i in range(1, 4):
        while True:
            raw = input(f"Enter score {i}: ").strip()
 
            # Make sure the input is actually a number
            if not raw.lstrip("-").isdigit():
                print("Invalid input. Please enter a whole number.")
                continue
 
            score = int(raw)
 
            if score < 0 or score > 100:
                print("Invalid score. Enter 0–100.") 
            
            else:
                scores.append(score)
                break  # Valid score collected; move on60
 
    # Build the student dictionary (average/grade/status added in Task 2)
    student = {
        "name": name,
        "scores": scores,
        "average": None,
        "grade": None,
        "status": None,
    }
 
    students.append(student)
    print("Student added.")
 
 
# Guard: nothing to process if no students were entered
if not students:
    print("\nNo students entered. Exiting.")
    exit()
 

#Average Calculation & Grade Assignment
 
for student in students:
    
    # Calculate average rounded to 1 decimal place
    
    average = round(sum(student["scores"]) / 3, 1)
 
    # Assign grade using if/elif/else
    
    if average >= 80:
        grade = "A"
    elif average >= 65:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"
 
    # Pass if average is 50 or above, otherwise Fail
    
    status = "PASS" if average >= 50 else "FAIL"
 
    # Update the student's dictionary with computed value
    
    student["average"] = average
    student["grade"] = grade
    student["status"] = status
 
 
#Find Top Performer — No max() Allowed
 
top_student = None
top_average = 0  # Tracking variable; any real average will beat this
 
for student in students:
    if student["average"] > top_average:
        top_average = student["average"]
        top_student = student
 
 

#Find Students with Special Score Conditions

failing_score_students = []   # At least one individual score < 40
perfect_score_students = []   # At least one individual score == 100
 
for student in students:
    for score in student["scores"]:
        if score < 40:
            # Add only once even if the student has multiple failing scores
            if student["name"] not in failing_score_students:
                failing_score_students.append(student["name"])
 
        if score == 100:
            if student["name"] not in perfect_score_students:
                perfect_score_students.append(student["name"])
 
 
#Calculate Class Average
total_averages = 0  # Accumulator
 
for student in students:
    total_averages += student["average"]
 
class_average = round(total_averages / len(students), 1)
 
 
#Generate Backend Report

print("\n========================================")
print("       STUDENT PERFORMANCE REPORT")
print("========================================")
 
for index, student in enumerate(students, start=1):
    print(f"{index}. {student['name']}")
    print(f"   Scores: {student['scores']}")
    print(f"   Average: {student['average']}")
    print(f"   Grade: {student['grade']}")
    print(f"   Status: {student['status']}")
 
print("========================================")
print(f"Class Average: {class_average}")
 
# Top performer line

if top_student:
    print(f"Top Performer: {top_student['name']} ({top_student['average']})")
 
# Show failing-score students or "None"

if failing_score_students:
    print(f"Students with failing scores: {', '.join(failing_score_students)}")
else:
    print("Students with failing scores: None")
 
# Show perfect-score students or "None"

if perfect_score_students:
    print(f"Students with perfect scores: {', '.join(perfect_score_students)}")
else:
    print("Students with perfect scores: None")
 
print("========================================")
 
 
# Search Feature
 
while True:
    query = input("\nEnter a student name to view details (or 'exit' to quit): ").strip()
 
    if query.lower() == "exit":
        print("Goodbye!")
        break  # End the search loop
 
    # Search case-insensitively through the students list
    
    found = False
    for student in students:
        if student["name"].lower() == query.lower():
            # Print the full record for the matched student
            print(f"Name:    {student['name']}")
            print(f"Scores:  {student['scores']}")
            print(f"Average: {student['average']}")
            print(f"Grade:   {student['grade']}")
            print(f"Status:  {student['status']}")
            found = True
        break  # No need to keep searching once found
 
    if not found:
        print("Student not found.")
