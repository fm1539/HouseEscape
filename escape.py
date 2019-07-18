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
            else:
                print('Sorry ' + answer + " is not the correct answer.")
                attempts_1 -= 1
                print("You have " + str(attempts_1) + ' attempts left.')
            answer = input('What is your guess?\n')
            
        