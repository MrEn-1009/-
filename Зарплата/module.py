def dopol(mon,inim):
    '''Добавляет нового человека и его зарплату
    '''
    while 1:
        use=input('Sisesta inimene:')
        if use not in inim:
            print('Tunnus soobib')
        zap=input('Sisesta raha:')
        mon.append(zap)
        inim.append(use)
        break
    return mon,inim
def koik(inim,mon):
	'''Показывает всех людей
    '''
	i=0
	for user in inim:
		print(user,end='-')
		print(mon[i])
		i+=1
def poisk(inim:list,mon:list):
    '''Tagastame jarjend või tekst
    :rtype var: tulemus
    '''
    nimi=(input('Keda otsime?'))
    for inimene in inim:
        if inimene==nimi:
            n=inim.count(nimi)
            print('Inimene on olemas,selline nimi kohtume',n,'korda')
            b=0
            t=[]
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
    a=input('Keda otsime?')
    if a not in inim:
        print('See nimi ei ole')
    else:
        b=inim.index(a)
        inim.remove(a)
        mon.pop(b)
def mox(mon:list,inim:list):
    '''Ищет максимальную сумму и кто её получает
    '''
    mom=max(mon)
    n=mon.count(mom)
    for i in mon:
        if i==mom:
            b=mon.index(i)
            break
    inil=inim[b]
    print(inil ,'-', mom)
