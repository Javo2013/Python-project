# question3.py

def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0

def get_letter_grade(average):
   
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def main():
    # ask how many scores to enter (use a while loop to validate)
    while True:
        try:
            count = int(input("How many test scores do you want to enter? "))
            if count <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    scores = []
    i = 0
    while i < count:
        try:
            s = float(input(f"Enter score {i + 1}: "))
            scores.append(s)
            i += 1
        except ValueError:
            print("Invalid score. Please enter a number.")

    average = calculate_average(scores)
    letter = get_letter_grade(average)

    print("\n=== GRADE REPORT ===")
    print(f"Test Scores: {scores}")
    print(f"Average Score: {average}")
    print(f"Letter Grade: {letter}")

if __name__ == "__main__":
    main()