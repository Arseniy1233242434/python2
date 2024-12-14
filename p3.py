import random
n=(2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,11,11,11,11)
b=list(n)
random.shuffle(b)
m=0
while True:
  v=(input("выберите действие "))
  if v=="n":
   print(f"ваше кол-во очков {m}")
   break
  elif(v=="y"):
    g=b.pop(1)
    m=m+g
    if m>21:
      print(f"вы проиграли, ваше кол-во очков {m}")
      break
    elif m==21:
      print(f"вы выиграли, ваше кол-во очков {m}")

