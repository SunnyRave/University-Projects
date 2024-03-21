N = int(input())

probabilities = []

for _ in range(N):
    password, probability = input().split()
    probabilities.append(float(probability))
probabilitiesdes = sorted(probabilities, reverse=True)
answer = 0
for i in range (len(probabilitiesdes)):
    answer = answer + probabilitiesdes[i] * (i+1)
print(answer)
    