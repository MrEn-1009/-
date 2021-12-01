from module import *
mon=[1200,2500,750,395,1200]
inim=['A','B','C','D','E']
while 1:
    b=input('0=Показать всех\n1=Lisa inimene\n2= \n')
    if b=='0':
        koik(inim,mon)
    elif b=='1':
        dopol(mon,inim)
    elif b=='2':
        vastus=poisk(inim,mon)
        print(vastus)
    elif b=='3':
        vastus=udal(inim,mon)
        print(vastus)
    elif b=='4':
        mox(mon,inim)