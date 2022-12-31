print('Welcome to my computer quiz')

playing = input('Do you want to play? ')  
print (playing)

if playing.lower() != 'yes':
    quit()
print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
     
                
answer = input("What does PDP stand for? ")
if answer.lower() == "people democratic party":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does APC stand for? ")
if answer.lower() == "all progressive congress":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print("You got " + str(score) + " questions correct!")


