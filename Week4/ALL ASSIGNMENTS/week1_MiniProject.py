#class number: B33

#Student score Analyser

# Creating a function to get A valid score
def get_score():
    while True:
        try:
            score = float(input("Enter a test score (0 - 100): "))

            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")

# Get the thre scores
score1 = get_score()
score2 = get_score()
score3 = get_score()

#calculate the Average
average = (score1 + score2 + score3) / 3

#Determine Pass or Fail
if average >= 50:
    result = "PASS"
else:
    result = "FAIL"

#Using F-strings to display results
print("\n----- STUDENT REPORT -----")
print(f"Score 1: {score1}")
print(f"Score 2: {score2}")
print(f"Score 3: {score3}")
print(f"Average: {average:.2f}")
print(f"Result: {result}")