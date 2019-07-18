print("Welcome to the escape room challenge!\n" "You wake up in an empty room with 4 doors.\n Each door leads to a different room: A for Green, B for blue, C for Yellow, D for Orange.\n One of the rooms leads to the path to escape. You have 3 attempts in the first room, and number of attempts decreases as you move from room to room. \nChoose wisely!\n")

start = input("Choose from the following doors: \n A\n B\n C\n D \n \n")
start = start.upper()

print(start)

if start == "A":
    print("Answer this riddle in under 3 attempts:\n What has a head, a tail, is brown, and has no legs?\n Hints: \n You see it everyday, but ignore it most of the time.\n It makes the world go round.\n Abraham Lincoln.\n")
    answer = input('What is your guess?\n')
    answer = answer.title()
    attempts_1 = 3
    if answer == 'Penny':
        print('Penny is the right answer! you may move on!\n ')
        move_n_1 = input('Enter e to move to room 2\n')
    else:
        while (answer!= 'Penny') or (attempts_1 > 1):
            
            if attempts_1 == 1:
                print('Sorry, you are trapped forever.')
                break
            else:
                print('Sorry ' + answer + " is not the correct answer.")
                attempts_1 -= 1
                print("You have " + str(attempts_1) + ' attempts left.')
            answer = input('What is your guess?\n')
if start == 'B':
    print("Can you name three consecutive days without using the words Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n (Seperate answers using only commas")
    answer = input('What is your guess?\n')
    answer = answer.title()
    attempts_1 = 3
    if answer == 'Yesterday, Today, Tomorrow':
        print('That is the right answer! you may move on!\n ')
        move_n_1 = input('Enter e to move to room 2\n')
    else:
        while (answer!= 'Yesterday, Today, Tomorrow') or (attempts_1 > 1):
            
            if attempts_1 == 1:
                print('Sorry, you are trapped forever.')
                break
            else:
                print('Sorry ' + answer + " is not the correct answer.")
                attempts_1 -= 1
                print("You have " + str(attempts_1) + ' attempts left.')
            answer = input('What is your guess?\n')
if start == 'C':
    print("David's father has three sons : Snap, Crackle and _____ ?")
    answer = input('What is your guess?\n')
    answer = answer.title()
    attempts_1 = 3
    if answer == 'David':
        print('That is the right answer! you may move on!\n ')
        move_n_1 = input('Enter e to move to room 2\n')
    else:
        while (answer!= 'David') or (attempts_1 > 1):
            
            if attempts_1 == 1:
                print('Sorry, you are trapped forever.')
                break
            else:
                print('Sorry ' + answer + " is not the correct answer.")
                attempts_1 -= 1
                print("You have " + str(attempts_1) + ' attempts left.')
            answer = input('What is your guess?\n')
if start == 'D':
    print("What comes down but never goes up")
    answer = input('What is your guess?\n')
    answer = answer.title()
    attempts_1 = 3
    if answer == 'Rain':
        print('Rain is the right answer! you may move on!\n ')
        move_n_1 = input('Enter e to move to room 2\n')
    else:
        while (answer!= 'David') or (attempts_1 > 1):
            
            if attempts_1 == 1:
                print('Sorry, you are trapped forever.')
                break
            else:
                print('Sorry ' + answer + " is not the correct answer.")
                attempts_1 -= 1
                print("You have " + str(attempts_1) + ' attempts left.')
            answer = input('What is your guess?\n')

    
            
            
            
        