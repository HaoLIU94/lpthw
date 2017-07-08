import random
cont=1
while cont==1:
    dice=[1,2,3,4,5,6]
    res = random.randint(dice[0], dice[5])
    print 'The result id',res
    print 'Would you like to play again'
    s = raw_input()
    if s =='yes':
        cont=0
    elif s=='no' :
        cont=1
    else:
        pass

