import random
cont=1
while cont==1:
    dice=[1,2,3,4,5,6]
    res = random.randint(1,6)
    print 'The result is',res
    print 'Would you like to play again'
    s = raw_input('yes/no\n')
    if s =='yes':
        cont=0
    elif s=='no' :
        cont=1
    else:
        pass

