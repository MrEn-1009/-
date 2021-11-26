def dopol(mon,inim):
    '''
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
	'''
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
    '''
    '''
    a=input('Keda otsime?')
    if a not in inim:
        print('See nimi ei ole')
    else:
        b=inim.index(a)
        inim.remove(a)
        mon.pop(b)
def max()

