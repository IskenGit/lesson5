class Store():

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, product, price):
        self.items[product] = price
        print(f"Товар {product} добавлен с ценой {price}.")

    def get_price(self, product):
        return self.items.get(product, None)

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
            print(f"Товар {product} удален.")
        else:
            print(f"Товар {product} не найден.")

    def update_price(self, product, new_price):
        if product in self.items:
            self.items[product] = new_price
            print(f"Цена товара {product} обновлена на {new_price}.")
        else:
            print(f"Товар {product} не найден.")

# Пример использования
store1 = Store("Vegetables", "123 Manasa St")
store1.add_item("potato", 50)
store1.add_item("tomatos", 75)
store1.add_item("cucumber", 60)

store2 = Store("Fruits", "58 Novator St")
store2.add_item("apples", 25)
store2.add_item("bananas", 40)

store3 = Store("Bakery", "169 Gagarina St")
store3.add_item("bread", 45)
store3.add_item("cake", 80)

x = store1.get_price("cucumber")
print(f"цена cucumber составляет {x} сомов")
y = store2.get_price("apples")
print(f"цена apples составляет {y} сомов")
z = store3.get_price("cake")
print(f"цена cake составляет {z} сомов")

store2.update_price("apples", 30)

store2.remove_item("bananas")

