# Name      : Andrew Devito Aryo
# NPM       : 2306152494
# TA Code   : GAN

# Take input for Student's First and Last Name
name = input("Enter name: ").title()

# Take input for three exams
exam1 = int(input("Enter the score for Exam 1: "))
exam2 = int(input("Enter the score for Exam 2: "))
exam3 = int(input("Enter the score for Exam 3: "))

# Calculate the average and total grade
# Using string formatting to display only 2 digits after decimal point
average_exam = f"{((exam1 + exam2 + exam3) / 3):.2f}"

total_exam = str(exam1 + exam2 + exam3)

# Take the total seconds as input
total_seconds = int(input("Enter the total seconds taken for the exams: "))

# Calculate the hours, minutes, and remaining seconds
# Use the operators // and %
hours       = str(total_seconds // 3600)              # Get Hours by divide-floor total_seconds by 3600 (1 hour = 3600 seconds)
minutes     = str((total_seconds % 3600) // 60)       # Get Minutes by get the remainder of total_seconds divided by 3600, and then divide-floor it by 60 (1 Minutes = 60 seconds)
seconds     = str((total_seconds % 3600) % 60)        # Get Seconds by get the remainder of total_seconds divided by 3600, and then get the remainder of it divided by 60

# Format and print the feedback messages
# Message 1
print("\n---", name, "---")
print("Exam Scores:", str(exam1) + ", " + str(exam2) + ", " + str(exam3))
print("Total Scores:", total_exam)
print("Average Score:", average_exam)
print("Time taken:", hours, "Hours", minutes, "Minutes", seconds, "Seconds")

# Message 2
print("\n--- Message for", name, "---")
print("Hey, " + name + ". You got exam scores of " 
      + str(exam1) + ", " + str(exam2) + ", and " + str(exam3) + " with total of "
      + total_exam + " and average of " + average_exam + ". The total time taken is " 
      + hours + " Hours " + minutes + " Minutes " + seconds + " Seconds.")