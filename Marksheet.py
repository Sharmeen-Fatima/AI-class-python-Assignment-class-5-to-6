# In below code we learn If, else, elif, and create a
# marksheet statement you write percentage to below you see you grade.

name = str(input("What's your name? "))
fathername = str(input("What's your father name? "))
Study = str(input("What your class? "))
subject = str(input("What's subject like/Biology/science? "))
marks = int(input("Write your marks out of 250: "))
Percentage = int((marks * 100) / 250)  # Calculate percentage and convert to integer
print(f"You got {Percentage}%")  # Use f-string to display the result
if Percentage >= 80:
    print(f"{name} your father name is {fathername} your study in class {Study} your learn {subject} subject in your class. Your numbers are 250/{marks} and your percentage is {Percentage}. Marvelous! You got Grade 'A+'.")
elif Percentage >= 70:
    print(f"{name} your father name is {fathername} your study in class {Study} your learn {subject} subject in your class. Your numbers are 250/{marks} and your percentage is {Percentage}. Excellent! You got Grade 'A'.")
elif Percentage >= 60:
    print(f"{name} your father name is {fathername} your study in class {Study} your learn {subject} subject in your class. Your numbers are 250/{marks} and your percentage is {Percentage}. Good Work! You got Grade 'B'.")
elif Percentage >= 50:
    print(f"{name} your father name is {fathername} your study in class {Study} your learn {subject} subject in your class. Your numbers are 250/{marks} and your percentage is {Percentage}. You need more practice. You got Grade 'C'.")
elif Percentage >= 40:
    print(f"{name} your father name is {fathername} your study in class {Study} your learn {subject} subject in your class. Your numbers are 250/{marks} and your percentage is {Percentage}. Doing Work Hard. You got Grade 'D'.")
elif Percentage >= 30:
    print(f"{name} your father name is {fathername} your study in class {Study} your learn {subject} subject in your class. Your numbers are 250/{marks} and your percentage is {Percentage}. You Grade is 'E'. Do more learn and hard work.")
else:
    print("Do more practice. Your grade is not found. I think you are fail. Oh no...")
