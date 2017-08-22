import random

while 1:
    num=random.randint(0,100)
    step=0
    while 1:
        step+=1
        guess=int(input('Input your guess\n'))
        #print num,guess
        if num>guess:
            print'Your number is smaller'
        elif num<guess:
            print'Your number is bigger'
        elif num==guess:
            print'Congulations, you win!!!'
            raw_input('Press key to continue\n')