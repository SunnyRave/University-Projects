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
    count2=[]
    count3=[]
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
    print('The roll is: ',L[0],L[1],L[2],L[3],L[4])
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
        e=b.split()
        if(e[0].lower()!='all' and len(e)!=5):
            if(set(e).issubset(set(L))): 
                g=1
            else: 
                g=0
            if(g==0): 
                print('That is not possible, try again!')
        elif(len(e)!=5 and e[0].lower()=='all'):  
            print('Ok, done')
            g=2
        elif(len(e)==5 and e[0].lower()!='all'):
            if(set(e).issubset(set(L))): 
                g=1
                print('Ok, done')
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
        print('The roll is: ',e[0],e[1],e[2],e[3],e[4])
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
        while(x==0): 
            b = str(input('Which dice do you want to keep for the third roll? ')).strip()
            t=b.split()
            if(t[0].lower()!='all' and len(t)!=5):
                if(set(t).issubset(set(e))): 
                    x=1
                else: 
                    x=0
                if(x==0): 
                    print('That is not possible, try again!')
            elif(len(t)!=5 and t[0].lower()=='all'):  
                print('Ok, done')
                x=2
            elif(len(t)==5 and t[0].lower()!='all'):
                if(set(t).issubset(set(e))): 
                    x=1
                    print('Ok, done')
                else: 
                    x=0
                if(x==0): 
                    print('That is not possible, try again!')
                    
            
        
        if(len(t)!=5 and x!=2): 
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
            print('The roll is: ',t[0],t[1],t[2],t[3],t[4])
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

  
# DEFINE OTHER FUNCTIONS
rectangles = [
    [(-15,0), (-15,10), (5,10), (5,0)],  # Rectangle 1
    [(-5,8), (-5,25), (20,25), (20,8)],  # Rectangle 2
    [(15,-4), (15,14), (24,14), (24,-4)],  # Rectangle 3
    [(0,-6), (0,4), (16,4), (16,-6)],  # Rectangle 4
    [(2,15), (2,22), (10,22), (10,15)],  # Rectangle 5
    [(30,10), (30,20), (36,20), (36,10)],  # Rectangle 6
    [(34,0), (34,16), (40,16), (40,0)]   # Rectangle 7