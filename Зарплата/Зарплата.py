from module import *
mon=[1200,2500,750,395,1200]
inim=['A','B','C','D','E']
while 1:
    b=input('1=Показать всех\n2=Добавить пользователя\n3=Поиск зарплаты по имени человека\n4=Удаление пользователя\n5=Максимальная зарплата и кто её получает')
    if b=='1':
        koik(inim,mon)
    elif b=='2':
        dopol(mon,inim)
    elif b=='3':
        vastus=poisk(inim,mon)
        print(vastus)
    elif b=='4':
        vastus=udal(inim,mon)
        print(vastus)
    elif b=='5':
        mox(mon,inim)