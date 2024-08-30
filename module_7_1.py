class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r', encoding='UTF-8')
        products = file.read()
        file.close()
        return products

    # Если файл не найден, возвращаем пустую строку.

    def add(self, *products):
        current_products = self.get_products()
        file = open(self.__file_name, 'a', encoding='UTF-8')
        for product in products:
            if str(product) not in current_products:
                file.write(str(product)+"\n")
                current_products+= str(product)+"\n"
            else:
                print(f"Продукт {product} уже есть в магазине")
        file.close()






if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())

