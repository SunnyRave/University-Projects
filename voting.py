i = int(input())
for _ in range(i):
    N, V1, V2, W = map(int, input().split())
    M = V1 + V2
    remaining= N - M
    if remaining % 2 == 0:
        V1 = V1 + (remaining//2)
        V2 = V2 + (remaining//2)
    else:
        V1 = V1 + (remaining//2) + 1 
        V2 = V2 + (remaining//2)
    if (V1/N)*100 > W and (V2/N)*100 < W:
        print("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!")
    elif (V1/N)*100 < W and (V2/N)*100 > W:
        print("RECOUNT!")
    elif (V1/N)*100 <= W and (V2/N)*100 <= W:
        print("PATIENCE, EVERYONE!")
    elif (V2/N)*100 >= W and (V1/N)*100 >= W:
        print("PATIENCE, EVERYONE!")
    