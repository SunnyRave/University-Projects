from random import randint
def play():
    i=0
    x=0
    e=[]
    e1=0
    L=[]
    t=[]
    count1=[]
    g=0
    j=0
    count2=[]
    count3=[]
    Q=[]
    for i in range(0,5):
        a = randint(0,5)
        if(a==0):
            L.append('Ace')
            continue
        elif(a==1):
            L.append('King')
            continue
        elif(a==2):
            L.append('Queen')
            continue
        elif(a==3):
            L.append('Jack')
            continue
        elif(a==4):
            L.append('10')
            continue
        elif(a==5):
            L.append('9')
            continue
    for x in L:
        if(x=='Ace'):
            Q.append(0)
        if(x=='King'):
            Q.append(1)
        if(x=='Queen'):
            Q.append(2)
        if(x=='Jack'):
            Q.append(3)
        if(x=='10'):
            Q.append(4)
        if(x=='9'):
            Q.append(5)
    L=[]
    Q.sort()
    for x in Q:
        if(x==0):
            L.append('Ace')
        if(x==1):
            L.append('King')
        if(x==2):
            L.append('Queen')
        if(x==3):
            L.append('Jack')
        if(x==4):
            L.append('10')
        if(x==5):
            L.append('9')
    print('The roll is:',L[0],L[1],L[2],L[3],L[4])
    countace = L.count('Ace')
    count1.append(countace)
    countking = L.count('King')
    count1.append(countking)
    countqueen = L.count('Queen')
    count1.append(countqueen)
    countjack = L.count('Jack')
    count1.append(countjack)
    count10=L.count('10')
    count1.append(count10)
    count9=L.count('9')
    count1.append(count9)
    if(5 in count1):
        print('It is a Five of a kind')
    elif(4 in count1):
        print('It is a Four of a kind')
    elif(3 in count1 and 2 in count1):
        print('It is a Full house')
    elif((('King' in L) and ('Queen' in L) and ('Jack' in L) and ('10' in L)) and (('Ace' in L) or ('9' in L))):
        print('It is a Straight')
    elif(3 in count1 and 2 not in count1):
        print('It is a Three of a kind')
    elif(count1.count(2)==2):
        print('It is a Two pair')
    elif(count1.count(2)==1 and count1.count(3)!=1):
        print('It is a One pair')
    elif((('Ace' in L) and ('9' in L)) and ((3 not in count1) and (2 not in count1) and (4 not in count1))):
        print('It is a Bust')
    while(g==0): 
        b = str(input('Which dice do you want to keep for the second roll? ')).strip()
        e=list(b.split())
        if(e==[]):
            g==1
            break
        if(e[0] not in ('all', 'All') and len(e)!=5):
            if(set(e).issubset(set(L))): 
                g=1
            else: 
                g=0
            if(g==0): 
                print('That is not possible, try again!')
        elif(len(e)!=5 and e[0] in ('all', 'All') and len(e)==1):  
            print('Ok, done.')
            g=2
        elif(e[0] in ('all','All') and len(e)!=1):
            g=0
            print('That is not possible, try again!')
        elif(len(e)==5 and e[0] not in ('all', 'All')):
            if(set(e).issubset(set(L))): 
                g=1
                print('Ok, done.')
            else: 
                g=0
            if(g==0): 
                print('That is not possible, try again!')
            
    
    if(len(e)!=5 and g!=2): 
        for e1 in range(0,5-len(e)):
            a = randint(0,5)
            if(a==0):
                e.append('Ace')
                continue
            elif(a==1):
                e.append('King')
                continue
            elif(a==2):
                e.append('Queen')
                continue
            elif(a==3):
                e.append('Jack')
                continue
            elif(a==4):
                e.append('10')
                continue
            elif(a==5):
                e.append('9')
                continue
        Q=[]
        for x in e:
            if(x=='Ace'):
                Q.append(0)
            if(x=='King'):
                Q.append(1)
            if(x=='Queen'):
                Q.append(2)
            if(x=='Jack'):
                Q.append(3)
            if(x=='10'):
                Q.append(4)
            if(x=='9'):
                Q.append(5)
        e=[]
        Q.sort()
        for x in Q:
            if(x==0):
                e.append('Ace')
            if(x==1):
                e.append('King')
            if(x==2):
                e.append('Queen')
            if(x==3):
                e.append('Jack')
            if(x==4):
                e.append('10')
            if(x==5):
                e.append('9')
        print('The roll is:',e[0],e[1],e[2],e[3],e[4])
        countace = e.count('Ace')
        count2.append(countace)
        countking = e.count('King')
        count2.append(countking)
        countqueen = e.count('Queen')
        count2.append(countqueen)
        countjack = e.count('Jack')
        count2.append(countjack)
        count10=e.count('10')
        count2.append(count10)
        count9=e.count('9')
        count2.append(count9)
        if(5 in count2):
            print('It is a Five of a kind')
        if(4 in count2):
            print('It is a Four of a kind')
        if(3 in count2 and 2 in count2):
            print('It is a Full house')
        if((('King' in e) and ('Queen' in e) and ('Jack' in e) and ('10' in e)) and (('Ace' in e) or ('9' in e))):
            print('It is a Straight')
        if(3 in count2 and 2 not in count2):
            print('It is a Three of a kind')
        if(count2.count(2)==2):
            print('It is a Two pair')
        if(count2.count(2)==1 and count2.count(3)!=1):
            print('It is a One pair')
        if((('Ace' in e) and ('9' in e)) and ((3 not in count2) and (2 not in count2) and (4 not in count2))):
            print('It is a Bust')
        while(j==0): 
            b = str(input('Which dice do you want to keep for the third roll? ')).strip()
            t=list(b.split())
            if(t==[]):
                j==1
                break
            if(t[0] not in ('all', 'All') and len(t)!=5):
                if(set(t).issubset(set(e))): 
                    j=1
                else: 
                    j=0
                if(j==0): 
                    print('That is not possible, try again!')
            elif(len(t)!=5 and t[0] in ('all', 'All') and len(t)==1):  
                print('Ok, done.')
                j=2
            elif(t[0] in ('all','All') and len(t)!=1):
                j=0
                print('That is not possible, try again!')
            elif(len(t)==5 and t[0] not in ('all', 'All')):
                if(set(t).issubset(set(e))): 
                    j=1
                    print('Ok, done.')
                else: 
                    j=0
                if(j==0): 
                    print('That is not possible, try again!')
                    
            
        
        if(len(t)!=5 and j!=2): 
            for t1 in range(0,5-len(t)):
                a = randint(0,5)
                if(a==0):
                    t.append('Ace')
                    continue
                elif(a==1):
                    t.append('King')
                    continue
                elif(a==2):
                    t.append('Queen')
                    continue
                elif(a==3):
                    t.append('Jack')
                    continue
                elif(a==4):
                    t.append('10')
                    continue
                elif(a==5):
                    t.append('9')
                    continue 
            Q=[]
            for x in t:
                if(x=='Ace'):
                    Q.append(0)
                if(x=='King'):
                    Q.append(1)
                if(x=='Queen'):
                    Q.append(2)
                if(x=='Jack'):
                    Q.append(3)
                if(x=='10'):
                    Q.append(4)
                if(x=='9'):
                    Q.append(5)
            t=[]
            Q.sort()
            for x in Q:
                if(x==0):
                    t.append('Ace')
                if(x==1):
                    t.append('King')
                if(x==2):
                    t.append('Queen')
                if(x==3):
                    t.append('Jack')
                if(x==4):
                    t.append('10')
                if(x==5):
                    t.append('9')
            print('The roll is:',t[0],t[1],t[2],t[3],t[4])
            countace = t.count('Ace')
            count3.append(countace)
            countking = t.count('King')
            count3.append(countking)
            countqueen = t.count('Queen')
            count3.append(countqueen)
            countjack = t.count('Jack')
            count3.append(countjack)
            count10=t.count('10')
            count3.append(count10)
            count9=t.count('9')
            count3.append(count9)
            if(5 in count3):
                print('It is a Five of a kind')
            if(4 in count3):
                print('It is a Four of a kind')
            if(3 in count3 and 2 in count3):
                print('It is a Full house')
            if((('King' in t) and ('Queen' in t) and ('Jack' in t) and ('10' in t)) and (('Ace' in t) or ('9' in t))):
                print('It is a Straight')
            if(3 in count3 and 2 not in count3):
                print('It is a Three of a kind')
            if(count3.count(2)==2):
                print('It is a Two pair')
            if(count3.count(2)==1 and count3.count(3)!=1):
                print('It is a One pair')
            if((('Ace' in t) and ('9' in t)) and ((3 not in count3) and (2 not in count3) and (4 not in count3))):
                print('It is a Bust')
    
    
        
            
            
                
    
        
    
                
    
    
        
                
        
    
            

    # REPLACE PASS ABOVE WITH YOUR CODE

def simulate(n):
    i=0
    Five_of_Hand=0
    Four_of_Hand=0
    Full_House=0
    Straight=0
    Three_of_Hand=0
    Two_Pair=0
    One_Pair=0
    Bust=0
    for i in range(0, n):
        L=[]
        count1=[]
        for s in range(0,5): 
            a = randint(0,5)
            if(a==0):
                L.append('Ace')
                continue
            elif(a==1):
                L.append('King')
                continue
            elif(a==2):
                L.append('Queen')
                continue
            elif(a==3):
                L.append('Jack')
                continue
            elif(a==4):
                L.append('10')
                continue
            elif(a==5):
                L.append('9')
                continue 
        countace = L.count('Ace')
        count1.append(countace)
        countking = L.count('King')
        count1.append(countking)
        countqueen = L.count('Queen')
        count1.append(countqueen)
        countjack = L.count('Jack')
        count1.append(countjack)
        count10=L.count('10')
        count1.append(count10)
        count9=L.count('9')
        count1.append(count9)
        if(5 in count1):
            Five_of_Hand= Five_of_Hand+1
        elif(4 in count1):
            Four_of_Hand=Four_of_Hand+1
        elif(3 in count1 and 2 in count1):
            Full_House=Full_House+1
        elif((('King' in L) and ('Queen' in L) and ('Jack' in L) and ('10' in L)) and (('Ace' in L) or ('9' in L))):
            Straight=Straight+1
        elif(3 in count1 and 2 not in count1):
            Three_of_Hand=Three_of_Hand+1
        elif(count1.count(2)==2):
            Two_Pair=Two_Pair+1
        elif(count1.count(2)==1 and count1.count(3)!=1):
            One_Pair=One_Pair+1
        elif((('Ace' in L) and ('9' in L)) and ((3 not in count1) and (2 not in count1) and (4 not in count1))):
            Bust=Bust+1
    Five_of_Hand=(Five_of_Hand/n)*100
    Four_of_Hand=(Four_of_Hand/n)*100
    Full_House=(Full_House/n)*100
    Straight=(Straight/n)*100
    Three_of_Hand=(Three_of_Hand/n)*100
    Two_Pair=(Two_Pair/n)*100
    One_Pair=(One_Pair/n)*100
    
    print(f'Five of a kind : {Five_of_Hand:.2f}%')
    print(f'Four of a kind : {Four_of_Hand:.2f}%')
    print(f'Full house     : {Full_House:.2f}%')
    print(f'Straight       : {Straight:.2f}%')
    print(f'Three of a kind: {Three_of_Hand:.2f}%')
    print(f'Two pair       : {Two_Pair:.2f}%')
    print(f'One pair       : {One_Pair:.2f}%')
    

    # REPLACE PASS ABOVE WITH YOUR CODE
play()

# DEFINE OTHER FUNCTIONS