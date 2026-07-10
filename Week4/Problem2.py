# problem2.py — TechRise Student Grade Processor


def validate_scores(*scores):
    """
    Check each score. Returns (valid_scores, invalid_entries).
    Valid scores are numbers between 0 and 100.
    """
    valid = []
    invalid = []

    for score in scores:
        try:
            value = float(score)   # try converting to a number
            if 0 <= value <= 100:
                valid.append(value)
            else:
                print(f"Warning: {score!r} is out of range (0–100).")
                invalid.append(score)
        except (ValueError, TypeError):
            print(f"Warning: {score!r} is not a valid score.")
            invalid.append(score)

    return valid, invalid


def get_grade(average):
    """Return the letter grade for a given average score."""
    if not (0 <= average <= 100):
        raise ValueError("Average must be between 0 and 100.")

    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    raw = (85, "pass", 72, 101, 63, None, 55)

    valid, invalid = validate_scores(*raw)

    avg   = sum(valid) / len(valid)
    grade = get_grade(avg)

    print(f"\nAverage: {avg:.2f} | Grade: {grade}")   # Average: 68.75 | Grade: B
