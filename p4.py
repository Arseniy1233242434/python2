input_string = input("Введите строку символов, разделенных пробелами: ")
c = input_string.split()
g = {}  
for char in c:
        if char in g:
            g[char].append(char)
        else:
            g[char] = [char]

t = list(g.values())
print("Вложенный список:", t)