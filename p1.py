import random
n = random.randint(1, 10)
t=0
while True:
    f=int(input("введите число"))
    t=t+1
    if(f==n):
        print(f"Вы угадали число за {t} попыток")
        break

    elif f<n:
        print("число меньше заданного")
    else:
        print("число больше заданного")
    4