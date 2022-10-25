# a dictionary that store question and answers
# Have a variable that track the score of the player
# Loop through the dictionary using the values pairs
# Display each question to the user and allow them to answer
# tell them if they are right or wrong
# Show the final result when quiz is completed

from question import quiz

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer? ")

    if answer.lower() == value["answer"].lower():
        print("Correct")
        score += 1
        print(f"Your score is: {score}")

    else:
        print("Wrong!")
        print("The answer is: ", value["answer"])
        print(f"Your score is: {score}")
