# Simple Quiz Game
print("=== Python Mini Quiz ===")
score = 0

# Question 1
ans1 = input("1. What is the extension for Python files? ")
if ans1.lower().strip() == ".py":
    print("Correct!")
    score += 1
else:
    print("Wrong! It is .py")

# Question 2
ans2 = input("2. What command prints output in Python? ")
if ans2.lower().strip() == "print":
    print("Correct!")
    score += 1
else:
    print("Wrong! It is print")
#Question 3
ans3 = input("3. Which keyword is used to return a value in C? ")
if ans3.lower().strip() == "return":
    print("Correct!")
    score += 1
else:
    print("Wrong! It is return")
  #Question 4
ans4 = input("4. Which symbol is used for comments in Python? (# or //) ")
if ans4.strip() == "#":
    print("Correct!")
    score += 1
else:
    print("Wrong! It is #")

print("=========final score board==========")
print(f"\nYour final score is: {score}/4")
