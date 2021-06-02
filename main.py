import random

# Computer
print("Computer Turn : Stone(1) , Paper(2) , Sizer(3)")

CompOption = random.randint(1, 3)
if CompOption == 1:
    computer = 'Stone'
elif CompOption == 2:
    computer = 'Paper'
else:
    computer = 'Sizer'

# User

UserInput = input("Your Turn: Stone(1) , Paper(2) , Sizer(3)")

if UserInput == 1:
    user = 'Stone'
elif UserInput == 2:
    user = 'Paper'
else:
    user = 'Sizer'


# Game Functions

def gamewin(computer, user):
    if computer == user:
        return None

    elif computer == 'Stone':
        if user == 'Sizer':
            return True
        elif user == 'Paper':
            return False

    elif computer == 'Paper':
        if user == 'Stone':
            return True
        elif user == 'Sizer':
            return False

    elif computer == 'Sizer':
        if user == 'Stone':
            return False
        elif user == 'Paper':
            return True


GameFun = gamewin(computer, user)


# Result Exit == 'q':
print(f"Computer Choice : {computer}")
print(f"Your Choice: {user}")
if GameFun is None:
    print("The Game is Tie")
elif GameFun is False:
    print("You Win")
else:
    print("Computer Win")
# CMD Exit
input("Type enter to exit: ")