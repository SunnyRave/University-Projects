threenumbers = input().strip()
X, Y, N = map(int, threenumbers.split())



for i in range(1, N + 1):
    if i % X == 0 and i % Y != 0:
        print("Fizz")
    elif i % Y == 0 and i % X != 0:
        print("Buzz")
    elif i % Y == 0 and i % X == 0:
        print("FizzBuzz")
    elif i % Y != 0 and i % X != 0:
        print(i)
        