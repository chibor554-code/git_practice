#Continuation of Assighnment1
#Class Number B33

def grade_summary(*args, subject="General"):
    """
    Summarises a set of scores for a given subject.
 
    Parameters:
        *args       : Any number of numeric scores.
        subject (str): The subject name. Defaults to "General".
 
    Returns:
        A formatted summary string, or "No scores provided." if no scores
        were passed in.
    """
    if not args:
        return "No scores provided."
 
    highest = args[0]
    lowest  = args[0]
    total   = 0
 
    for score in args:
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
        total += score
 
    count   = len(args)
    average = round(total / count, 1)
 
    return (
        f"Subject: {subject} | "
        f"Scores: {count} | "
        f"Highest: {highest} | "
        f"Lowest: {lowest} | "
        f"Average: {average}"
    )
 
 
 
 
 # STUDENT CARD
 
def student_card(name, cohort, **kwargs):
    """
    Prints a formatted student card.
 
    Parameters:
        name   (str): The student's full name.
        cohort (int/str): The cohort number or label.
        **kwargs    : Any additional fields to display
                      (e.g. track, level, email).
    """
    # Combine the fixed fields with any extras
    fields = {"Name": name, "Cohort": cohort, **kwargs}
 
    for label, value in fields.items():
        # Capitalise the label and pad it to exactly 12 characters
        print(f"{label.capitalize():<12}: {value}")
 
 

# Tests
if __name__ == "__main__":
 
    # ── grade_summary ──────────────────────────
    print("=== grade_summary tests ===\n")
 
    # Test 1 – named subject, multiple scores
    print(grade_summary(92, 85, 78, 60, 66, subject="Mathematics"))
 
    # Test 2 – default subject
    print(grade_summary(55, 70, 83, 91))
 
    # Test 3 – single score
    print(grade_summary(74, subject="Physics"))
 
    # Test 4 – no scores
    print(grade_summary())
 
    # ── student_card ───────────────────────────
    print("\n=== student_card tests ===\n")
 
    # Test 1 – with several extra fields
    student_card(
        "Ada Okafor", 3,
        track="Data Engineering",
        level="Intermediate",
        email="ada@example.com"
    )
    
    print()
 
    # Test 2 – minimal extra fields
    student_card("Chidi Nwosu", 5, track="Backend Web")
 
    print()
 
    # Test 3 – different kwargs
    student_card(
        "Ngozi Eze", 2,
        track="Cybersecurity",
        level="Advanced",
        city="Lagos"
    )