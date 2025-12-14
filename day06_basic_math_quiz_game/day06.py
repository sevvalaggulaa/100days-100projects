#Basic Math Quiz Game
import random
import time

#Step 1: Define the math question function
def generate_question():

  num1 = random.randint(1, 20)
  num2 = random.randint(1, 20)
  operator = random.choice(['+', '-', '*', '/'])
    
  if operator == '+':
    answer = num1 + num2
  elif operator == '-':
    answer = num1 - num2
  elif operator == '/':
    while num1 % num2 != 0 or num2 == 0:
      num2 = random.randint(1, 10)
    answer = num1 // num2
  else:
    answer = num1 * num2

  return f"{num1} {operator} {num2}", answer

#Step 2: Main Quiz Game Function
def math_quiz():
  score = 0

  print("\n--- Welcome to the Math Quiz Game! ---")
  print("\nYou will be presented with math problems and you need to provide the correct answers. ")
  rounds = int(input("How many rounds do you want to play? "))
  print("\nStarting the quiz...")
  
  start_time = time.time()

  for i in range(rounds):
    question, correct_answer = generate_question()
    print(f"\nQuestion {i + 1}: {question}")
    user_answer = int(input("Your answer: "))

    if user_answer == correct_answer:
      print("Correct!")
      score += 1
    else:
      print(f"Wrong! The correct answer is {correct_answer}.")
  
  end_time = time.time()
  duration = end_time - start_time

  print("\n--- Quiz Completed! ---")
  print(f"Your final core is: {score}/{rounds}")
  print(f"Time taken: {duration:.2f} seconds")
  
  if score == rounds:
    print("Congratulations! You answered all the questions correctly!")
  elif score >= rounds // 2:
    print("Good job! You did well.")
  else:
    print("Keep practicing! You can do better next time.")

#Step 3: Run the Quiz Game
math_quiz()

    
