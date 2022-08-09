from abc import abstractmethod, ABC


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self, count):
        pass

    @abstractmethod
    def get_items(self, count):
        pass

    @abstractmethod
    def get_unique_items_count(self, count):
        pass


class Store(Storage):

    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, count):
        self.__capacity = count

    def add(self, name, count):
        if name in self.__items.keys():
            if self.get_free_space() >= count:
                self.__items[name] += count
                return True
            else:
                return False
        else:
            if self.get_free_space() >= count:
                print("Товар добавлен")
                self.__items[name] = count
                return True
            else:
                if isinstance(self, Shop):
                    print("Недостаточно места в магазине")
                if isinstance(self, Store):
                    print("Недостаточно места на складе")
                return False

    def remove(self, name, count):
        if self.__items[name] >= count:
            print("Нужное количество есть на складе")
            self.__items[name] -= count
            return True
        else:
            print("Недостаточно товара на складе")
            return False

    def get_free_space(self):
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space

    @property
    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items.keys())

    def __str__(self):
        st = ""
        for key, value in self.__items.items():
            st += f"{key}: {value}\n"
        return st


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):
        if self.get_unique_items_count() >= 5:
            return "Слишком много уникальных товаров"
        else:
            super().add(name, count)


class Request:
    def __init__(self, request_str):
        req_list = request_str.split()
        action = req_list[0]
        self.__count = int(req_list[1])
        self.__item = req_list[2]
        if action == "Доставить":
            self.__from = req_list[4]
            self.__to = req_list[6]
        elif action == "Забрать":
            self.__from = req_list[3]
            self.__to = None
        elif action == "Привезти":
            self.__to = req_list[3]
            self.__from = None

    def move(self):
        if self.__to and self.__from:
            eval(self.__from).remove(self.__item, self.__count)
            print(f"Курьер забрал {self.__count} {self.__item} со {self.__from}")
            eval(self.__to).add(self.__item, self.__count)
            print(f"Курьер везет {self.__count} {self.__item} со {self.__from} в {self.__to}")
            print(f"Курьер доставил {self.__count} {self.__item} в {self.__to}")
        elif self.__to:
            eval(self.__to).add(self.__item, self.__count)
            print(f"Курьер везет {self.__count} {self.__item} в {self.__to}")
        elif self.__from:
            eval(self.__from).remove(self.__item, self.__count)
            print(f"Курьер забрал {self.__count} {self.__item} со {self.__from}")


storage = Store(items={"Телефон": 10, "Компьютер": 10, "Телевизор": 10})

shop = Shop(items={"Телефон": 3, "Компьютер": 3, "Телевизор": 3})