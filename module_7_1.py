


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

        file = open(self.__file_name, 'r')
        content = file.read()
        file.close()

        return content

    def add(self, *products):
        existing_products = set() # создаем пустое множество, с которым будем сверять наличие продукта
        print ("existing_products:",existing_products)
        file = open(self.__file_name, 'w') #открываем файл для записи

        #file.seek(0)  # Перемещаемся к началу файла

        for product in products:
            if product.name not in existing_products:
                print(f"{product}")
                file.write(str(product) + '\n')
                existing_products.add(product.name)
            else:
                print(f"Продукт {product} уже есть в магазине")

        file.close()
        print("existing_products:", existing_products)



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print("продукт 2: ", p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
