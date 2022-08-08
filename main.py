from classes import storage, shop, Request

while True:
    print("В складе храниться:")
    print(f"{storage}")
    print("В магазине храниться:")
    print(f" {shop}")
    user_text = input("Введите команду:\n")
    if user_text == "стоп":
        break
    else:
        try:
            req = Request(user_text)
            req.move()
        except Exception as e:
            print(f"Произошла ошибка {e}, но не расстраивайтесь, играйте дальше!")


# Пользователь: Доставить 3 Компьютер из storage в shop

# Программа: Нужное количество есть на складе
# Программа: Курьер забрал 3 печеньки со склад
# Программа: Курьер везет 3 печеньки со склад в магазин
# Программа: Курьер доставил 3 печеньки в магазин

# Программа: В склад хранится:

# Программа: 3 печеньки
# Программа: 4 собачки
# Программа: 5 коробки

# Программа: В магазин хранится:

# Программа: 2 собачки
# Программа: 5 печеньки