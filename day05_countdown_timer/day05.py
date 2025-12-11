#Countdown Timer

import time

#Step 1: Get user input for countdown start
start=int(input("Enter the number to start the countdown from: "))
message = input("Enter a message to display when the countdown is complete: ")
delay = float(input("Enter the time in seconds between each countdown: "))

#Step 2: Countdown using a while-loop
print("\n---- Countdown Begins ----")
while start>0:
  print(start)
  time.sleep(delay)
  start -= 1

#Step 3: Print final message
print(f">>>>>>  {message}  <<<<<<")

