a = str(input("Введите строку: "))
b = a.split()

for word in b.copy():
    if not any(c.isalpha() for c in word):
        b.remove(word)

c = len(b)
print("Количество введенных слов равняется", c)



