import sys

# INSERT YOUR OWN FUNCTIONS
coordinates=[]
rangesx=[]
rangesy=[]
k=0
filename = input('Which data file do you want to use? ')
try:
    with open(filename) as file:
        for line in file:
            x1, y1, x2, y2 = map(int, line.split())
            coordinates.append([x1,y1])
            coordinates.append([x1,y2])
            coordinates.append([x2,y2])
            coordinates.append([x2,y1])
            if(x2>x1):
                rangesx.append([x2,x1])
            else:
                rangesx.append([x1,x2])
            if(y2>y1):
                rangesy.append([y2,y1])
            else:
                rangesy.append([y1,y2])

except FileNotFoundError:
    print('Could not open a file named', filename)
    print('Giving up...')
    sys.exit()
print(coordinates)
print(rangesx)
print(rangesy)
coordinates1 = []
for i in range(len(coordinates)):
    for j in range(len(rangesx)):
        if((coordinates[i][0] < rangesx[j][0] and coordinates[i][0] > rangesx[j][1]) and (coordinates[i][1] < rangesy[j][0] and coordinates[i][1] > rangesy[j][1])):
            break
    else:
        coordinates1.append(coordinates[i])


coordinates2 = [coordinates[i:i+4] for i in range(0, len(coordinates), 4)]


i=0
intercepts=[]
for i in range(0,len(coordinates2)):
    A=[]
    A = coordinates2[i]
    A.append(A[0])
    for j in range(i+1,len(coordinates2)):
        B=[]
        B= coordinates2[j]
        B.append(B[0])
        for k in range(0,4):
            for l in range(0,4):
                if(A[k][0]==A[k+1][0] and B[l][1]==B[l+1][1]):
                    if(B[l][0]>B[l+1][0]):
                        if((B[l][0]>A[k][0] and B[l+1][0]<A[k][0]) and ((B[l][1]>A[k][1] and B[l][1]<A[k+1][1]) or (B[l][1]<A[k][1] and B[l][1]>A[k+1][1]))):
                            intercepts.append([A[k][0],B[l][1]])
                        else:
                            continue
                    else:
                        if((B[l][0]<A[k][0] and B[l+1][0]>A[k][0]) and ((B[l][1]>A[k][1] and B[l][1]<A[k+1][1]) or (B[l][1]<A[k][1] and B[l][1]>A[k+1][1]))):
                            intercepts.append([A[k][0],B[l][1]])
                        else:
                            continue
                        
                elif(A[k][1]==A[k+1][1] and B[l][0]==B[l+1][0]):
                    if(B[l][1]>B[l+1][1]):
                        if((B[l][1]>A[k][1] and B[l+1][1]<A[k][1]) and ((B[l][0]>A[k][0] and B[l][0]<A[k+1][0]) or (B[l][0]<A[k][0] and B[l][0]>A[k+1][0]))):
                            intercepts.append([B[l][0],A[k][1]])
                        else:
                            continue
                    else:
                        if((B[l][1]<A[k][1] and B[l+1][1]>A[k][1]) and ((B[l][0]>A[k][0] and B[l][0]<A[k+1][0]) or (B[l][0]<A[k][0] and B[l][0]>A[k+1][0]))):
                            intercepts.append([B[l][0],A[k][1]])
                        else:
                            continue
                        
                elif(A[k][0]==A[k+1][0] and B[l][0]==B[l+1][0]):
                    continue
                elif(A[k][1]==A[k+1][1] and B[l][1]==B[l+1][1]):
                    continue
i=0
j=0
intercepts1=[]
for i in range(len(intercepts)):
    for j in range(len(rangesx)):
        if((intercepts[i][0] < rangesx[j][0] and intercepts[i][0] > rangesx[j][1]) and (intercepts[i][1] < rangesy[j][0] and intercepts[i][1] > rangesy[j][1])):
            break
    else:
        intercepts1.append(intercepts[i])     
                    
                     
i=0
j=0
units=[]
units2=[]
for i in range(0,len(rangesx)):
    units2.append(i)
    for j in range(i+1,len(rangesx)):
        if(((rangesx[i][0]>rangesx[j][0] and rangesx[i][1]<rangesx[j][0]) or (rangesx[i][0]>rangesx[j][1] and rangesx[i][1]<rangesx[j][1])) and ((rangesy[i][0]>rangesy[j][0] and rangesy[i][1]<rangesy[j][0]) or (rangesy[i][0]>rangesy[j][1] and rangesy[i][1]<rangesy[j][1]))):
            units.append(i)
            units.append(j)
        else:
            continue
units1 = [units[i:i+2] for i in range(0, len(units), 2)]
def group_connected(units1):
    groups = []
    for elem in units1:
        added = False
        for group in groups:
            if any(num in group for num in elem):
                group.update(elem)
                added = True
                break
        if not added:
            groups.append(set(elem))
    merged_groups = []
    while groups:
        current = groups.pop(0)
        overlap = set().union(*[g for g in groups if current.intersection(g)])
        if overlap:
            groups = [g for g in groups if not g.intersection(current)]
            current.update(overlap)
        merged_groups.append(current)
    return [list(group) for group in merged_groups]
connected = group_connected(units1)
distinct = [w1 for w1 in units2 if w1 not in units]
print(distinct)  
for w2 in distinct:
    connected.append([w2])
print(connected)
all_exterior_coordinates=coordinates1+intercepts1
print(all_exterior_coordinates)
perimeter=0
for e in connected:
    minrx=[]
    maxrx=[]
    minry=[]
    maxry=[]
    for e1 in e:
        minrx.append(rangesx[e1][1])
        maxrx.append(rangesx[e1][0])
        maxry.append(rangesy[e1][0])
        minry.append(rangesy[e1][1])
    minx=min(minrx)
    maxx=max(maxrx)
    miny=min(minry)
    maxy=max(maxry)
    print(minx)
    print(maxx)
    print(miny)
    print(maxy)
    all_exterior_points=[]
    for h in range(0,len(all_exterior_coordinates)):
        if((all_exterior_coordinates[h][0]<=maxx and all_exterior_coordinates[h][0]>=minx) and (all_exterior_coordinates[h][1]<=maxy and all_exterior_coordinates[h][1]>=miny)):
            all_exterior_points.append(all_exterior_coordinates[h])
            continue
        else:
            continue
    print(all_exterior_points)
    if(len(all_exterior_points) < 4):
        continue
    leftmost_points=[]
    bottom_leftmost_points=[]
    for d in range(0,len(all_exterior_points)):
        if(all_exterior_points[d][0]==minx):
            leftmost_points.append(all_exterior_points[d])
    for d1 in range(0,len(leftmost_points)):
        bottom_leftmost_points.append(leftmost_points[d1][1])
    bottompoint=min(bottom_leftmost_points)
    current_location=[]
    current_location.append([minx,bottompoint])
    print(current_location)
    direction='Right'
    flag=1
    origin=[]
    origin.append(current_location[0])
    print(origin)
    while(all_exterior_points!=[]):
        if(direction == 'Right'):
            next_point = any(sublist[1] > current_location[0][1] and sublist[0] == current_location[0][0] for sublist in all_exterior_points)
            if(next_point==True):
                result=[]
                result_sorted=[]
                x11=[]
                b1=0
                print(current_location)
                print(direction)
                result = [x11 for x11 in all_exterior_points if x11[0] == current_location[0][0] and x11[1]>current_location[0][1]]
                yvalues=[]
                for b1 in range(0,len(result)):
                    yvalues.append(result[b1][1])
                yvalue=min(yvalues)
                result_sorted.append([current_location[0][0],yvalue])
                perimeter = perimeter+(result_sorted[0][1]-current_location[0][1])
                print(perimeter)
                
                direction='Up'
                if(current_location[0]!=origin[0]): 
                    all_exterior_points.remove(current_location[0])
                print(all_exterior_points)
                current_location=[]
                current_location.append(result_sorted[0])
                flag=0
                
                
                    
            elif(next_point==False):
                result=[]
                result_sorted=[]
                x11=[]
                b1=0
                print(current_location)
                print(direction)
                result = [x11 for x11 in all_exterior_points if x11[0] == current_location[0][0] and x11[1]<current_location[0][1]]
                yvalues=[]
                for b1 in range(0,len(result)):
                    yvalues.append(result[b1][1])
                yvalue=min(yvalues)
                result_sorted.append([current_location[0][0],yvalue])
                perimeter = perimeter+(current_location[0][1]-result_sorted[0][1])
                print(perimeter)
                
                direction='Down'
                all_exterior_points.remove(current_location[0])
                print(all_exterior_points)
                current_location=[]
                current_location.append(result_sorted[0])
                flag=0
        if(direction == 'Left'):
            next_point = any(sublist[1] < current_location[0][1] and sublist[0] == current_location[0][0] for sublist in all_exterior_points)
            if(next_point==True):
                result=[]
                result_sorted=[]
                x11=[]
                b1=0
                print(current_location)
                print(direction)
                result = [x11 for x11 in all_exterior_points if x11[0] == current_location[0][0] and x11[1]<current_location[0][1]]
                yvalues=[]
                for b1 in range(0,len(result)):
                    yvalues.append(result[b1][1])
                yvalue=min(yvalues)
                result_sorted.append([current_location[0][0],yvalue])
                perimeter = perimeter+(current_location[0][1]-result_sorted[0][1])
                print(perimeter)
                
                direction='Down'
                all_exterior_points.remove(current_location[0])
                print(all_exterior_points)
                current_location=[]
                current_location.append(result_sorted[0])
                flag=0
                    
            elif(next_point==False):
                result=[]
                result_sorted=[]
                x11=[]
                b1=0
                print(current_location)
                print(direction)
                result = [x11 for x11 in all_exterior_points if x11[0] == current_location[0][0] and x11[1]>current_location[0][1]]
                yvalues=[]
                for b1 in range(0,len(result)):
                    yvalues.append(result[b1][1])
                yvalue=min(yvalues)
                result_sorted.append([current_location[0][0],yvalue])
                perimeter = perimeter+(result_sorted[0][1]-current_location[0][1])
                print(perimeter)
                
                direction='Up'
                all_exterior_points.remove(current_location[0])
                print(all_exterior_points)
                current_location=[]
                current_location.append(result_sorted[0])
                flag=0
        if(direction == 'Up'):
            next_point = any(sublist[1] == current_location[0][1] and sublist[0] < current_location[0][0] for sublist in all_exterior_points)
            if(next_point==True):
                result=[]
                result_sorted=[]
                x11=[]
                b1=0
                print(current_location)
                print(direction)
                result = [x11 for x11 in all_exterior_points if x11[0] < current_location[0][0] and x11[1]==current_location[0][1]]
                xvalues=[]
                for b1 in range(0,len(result)):
                    xvalues.append(result[b1][0])
                xvalue=min(xvalues)
                result_sorted.append([xvalue,current_location[0][1]])
                perimeter = perimeter+(current_location[0][0]-result_sorted[0][0])
                print(perimeter)
                
                direction='Left'
                all_exterior_points.remove(current_location[0])
                print(all_exterior_points)
                current_location=[]
                current_location.append(result_sorted[0])
                flag=0
                
                    
            elif(next_point==False):
                result=[]
                result_sorted=[]
                x11=[]
                b1=0
                print(current_location)
                print(direction)
                result = [x11 for x11 in all_exterior_points if x11[0] > current_location[0][0] and x11[1]==current_location[0][1]]
                xvalues=[]
                for b1 in range(0,len(result)):
                    xvalues.append(result[b1][0])
                xvalue=min(xvalues)
                result_sorted.append([xvalue,current_location[0][1]])
                perimeter = perimeter+(result_sorted[0][0]-current_location[0][0])
                print(perimeter)
        
                direction='Right'
                all_exterior_points.remove(current_location[0])
                print(all_exterior_points)
                current_location=[]
                current_location.append(result_sorted[0])
                flag=0
                
        if(direction == 'Down'):
            next_point = any(sublist[1] == current_location[0][1] and sublist[0] > current_location[0][0] for sublist in all_exterior_points)
            if(next_point==True):
                result=[]
                result_sorted=[]
                x11=[]
                b1=0
                print(current_location)
                print(direction)
                result = [x11 for x11 in all_exterior_points if x11[0] > current_location[0][0] and x11[1]==current_location[0][1]]
                xvalues=[]
                for b1 in range(0,len(result)):
                    xvalues.append(result[b1][0])
                xvalue=min(xvalues)
                result_sorted.append([xvalue,current_location[0][1]])
                perimeter = perimeter+(result_sorted[0][0]-current_location[0][0])
                print(perimeter)
        
                direction='Right'
                all_exterior_points.remove(current_location[0])
                print(all_exterior_points)
                current_location=[]
                current_location.append(result_sorted[0])
                flag=0
                
                    
            elif(next_point==False):
                result=[]
                result_sorted=[]
                x11=[]
                xvalues=[]
                b1=0
                print(current_location)
                print(direction)
                result = [x11 for x11 in all_exterior_points if x11[0] < current_location[0][0] and x11[1]==current_location[0][1]]
                
                for b1 in range(0,len(result)):
                    xvalues.append(result[b1][0])
                xvalue=min(xvalues)
                result_sorted.append([xvalue,current_location[0][1]])
                perimeter = perimeter+(current_location[0][0]-result_sorted[0][0])
                print(perimeter)
                
                direction='Left'
                all_exterior_points.remove(current_location[0])
                print(all_exterior_points)
                current_location=[]
                current_location.append(result_sorted[0])
                flag=0
        if(current_location[0]==origin[0] and flag==0 and all_exterior_points!=[]):
            
            all_exterior_points.remove(origin[0])
            if(all_exterior_points==[]):
                break
            leftmost_points=[]
            bottom_leftmost_points=[]
            result=[]
            d=0
            d1=0
            print(all_exterior_points)
            result=sorted(all_exterior_points, key=lambda x: x[0])
            minx1=result[0][0]
            for d in range(0,len(all_exterior_points)):
                if(all_exterior_points[d][0]==minx1):
                    leftmost_points.append(all_exterior_points[d])
            for d1 in range(0,len(leftmost_points)):
                bottom_leftmost_points.append(leftmost_points[d1][1])
            bottompoint1=min(bottom_leftmost_points)
            current_location=[]
            current_location.append([minx1,bottompoint1])
            origin=[]
            origin.append(current_location[0])
            flag=1
            direction='Right'
            print(origin)
            
print('The perimeter is:',perimeter)     
            
            
        
        
        
                    
                    
                    
                                          
            
            
        
        
        

    
        