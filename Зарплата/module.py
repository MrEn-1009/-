def dopol(mon,inim):
    '''Добавляет нового человека и его зарплату
    '''
    while 1: #бесконечный цикл
        use=input('Sisesta inimene:') #вводим челоека
        if use not in inim:     #проверка
            print('Tunnus soobib')
        zap=int(input('Sisesta raha:'))   #вводим сумму
        mon.append(zap)  #добавляем зарплату в список
        inim.append(use) #добавляем человека в список
        break #Заканчиваем бесконечный цикл
    return mon,inim #возвращяем списки
def koik(inim,mon): #создаём функцию
	'''Показывает всех людей
    '''
	i=0
	for user in inim:  #цикл с шагом 1
		print(user,end='-')  
		print(mon[i])
		i+=1
def poisk(inim:list,mon:list): 
    '''Tagastame jarjend või tekst
    :rtype var: tulemus
    '''
    nimi=(input('Keda otsime?'))  #вводим кого найти хотим
    for inimene in inim:  #цикл с поиском с списках
        if inimene==nimi:  #проверяем схожи ли имена
            n=inim.count(nimi)  #Проверяем сколько всего таких людей
            print('Inimene on olemas,selline nimi kohtume',n,'korda') #показываем пользователю сколько их
            b=0  
            t=[]  #создаем пустой списко
            for i in range(n): 
                k=inim.index(nimi,b) 
                palk=mon[k]
                b+=k+1
                t.append(nimi+str(palk))   
        else:
            t='Ei ole nimekirjas'
    return t
def udal(inim:list,mon:list):
    '''Удаляет пользователя и его зарплату
    '''
    a=input('Keda otsime?')  #спрашиваем человека
    if a not in inim:    #проверка
        print('See nimi ei ole')
    else:   
        b=inim.index(a)     #индекс нашли
        inim.remove(a)         #Удаляем из списка
        mon.pop(b)             #Удаляем его зарплату
def mox(mon:list,inim:list):
    '''Ищет максимальную сумму и кто её получает
    '''
    mom=max(mon)            #Поиск максимальной зарплаты
    for i in mon:           #ищём индекс зарплаты
        if i==mom:        
            b=mon.index(i)        #запоминаем данный индекс
            break
    inil=inim[b]                #находим человека и запомнаем его в виде переменной
    print(inil ,'-', mom)         #показываем данного человека и его зарплату
