import random
tesha = ['rr','kk','hh']
vova = ['kk']
evrei = ['ll']
d = {'dict': tesha[random.randint(0,2)], 'dictionary': vova}
while True:
    d = {'dict': tesha[random.randint(0, 2)], 'dictionary': vova}
    if input() == 't':
        print(d['dict'])