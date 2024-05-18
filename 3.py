tovar = input('Введите Наименование: ')
cena = input("Введите цену (руб): ")
ves= input("Введите вес (кг): ")
many = input('Внесите сумму (руб): ')
ves = float(ves)
cena = int(cena)
many = int(many)
summa = ves * cena
sdacha = many - summa
print("Чек")
print("Итого", summa, "руб.")
print("Внесено", many, "руб.")
print("Сдача", sdacha, "руб.")