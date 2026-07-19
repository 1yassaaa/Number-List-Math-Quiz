import random
import time

#random_list -> fucncttion
def random_list(quantity, minimum, maximum):
    numbers =[]
    for _ in range(quantity):
        numbers.append(random.randint(minimum, maximum))
    return numbers

#ask_question -> function
def ask_question(question, answer):
    print(question)
    while True:
        try:
            user_input = int(input("> "))
            break
        except:
            print("Error.Invalid input.Enter an int.")
    if user_input == answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! Correct answer was {answer}.")
        return False
      
##main program##
#welcome message
print("Welcome to Yasiru Senavirathna's (10740155) Number List Test!")

#Difficulty mode selection
print()
print("Select a difficulty: [E]asy, [M]edium, [H]ard.")
while True:
    difficulty = input("> ").lower()
    if difficulty in ['e', 'm', 'h']:
        break
    else:
        print("Invalid choice! Enter E, M or H.")

if difficulty == 'e':
    questions = 4
    quantity = 3
    minimum = 5
    maximum = 10
    print("Easy difficulty selected!")
elif difficulty == 'm':
    questions = 5
    quantity = 4
    minimum = 5
    maximum = 15
    print("Medium difficulty selected!")
elif difficulty == 'h':
    questions = 6
    quantity = 5
    minimum = 10
    maximum = 20
    print("Hard difficulty selected!")
else : print("Invalid choice! Enter E,M or H.")

print(f"\nYour test will have {questions} questions using lists of "
      f"{quantity} numbers between {minimum} and {maximum}.")
print("The last question is a challenge question with twice as many numbers!")
input("\nPress Enter to begin!") #new line 

score = 0
starting_time = time.time()

#question loop
for q in range(1, questions +1):

    #Last challenge question
    if q == questions:
        print("\n[!!!] Challenge Question [!!!]")
        current_quantity = quantity * 2
    else:
        current_quantity = quantity
 
    print(f"\nQuestion {q} of {questions}.") #new line
    numbers = random_list(current_quantity, minimum, maximum)
    print(numbers)
 
    q_type = random.randint(1, 4)
 
    # Question type 1 -> Sum
    if q_type == 1:
        correct = sum(numbers)
        if ask_question("What is the sum of the numbers in this list?", correct):
            score += 1
 
    # Questions type 2 -> Difference (max - min)
    elif q_type == 2:
        correct = max(numbers) - min(numbers)
        if ask_question("What is the difference between the minimum and maximum numbers in this list?", correct):
            score += 1
 
    # Question type 3 -> Count above average
    elif q_type == 3:
         avg = sum(numbers) // len(numbers) # // removes decimals
         correct = sum(1 for n in numbers if n > avg)
         if ask_question(f"How many numbers in this list are higher than {avg}?", correct):
             score += 1

    # Question type 4 -> Product positions 
    else:
        pos_1 = random.randint(1, len(numbers))
        while True:
            pos_2 = random.randint(1, len(numbers))
            if pos_2 != pos_1:
                break
        correct = numbers[pos_1 - 1] * numbers[pos_2 - 1]
        if ask_question(f"What is the product of the numbers in positions {pos_1} and {pos_2} in this list?", correct):
            score += 1

ending_time = time.time()
total_time = ending_time - starting_time
percentage = round((score / questions) *100)
average_time =round(total_time / questions, 2)

print(f"\nTest is Completed!  You took {round(total_time, 2)} seconds.")
print(f"You scored {percentage}% ({score}/{questions} questions correct).")
print(f"Average of {average_time} seconds per question.")

if score == questions:
    print("Perfect score, well done!")





        


         






