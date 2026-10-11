from collections.abc import Callable


class Product:
    def __init__(self, name: str, store: str, cost: float) -> None:
        self.__name = name
        self.__store = store
        self.__cost = cost

    @property
    def name(self) -> str:
        return self.__name

    @property
    def store(self) -> str:
        return self.__store

    @property
    def cost(self) -> float:
        return self.__cost

    @cost.setter
    def cost(self, value: float):
        if value > 0:
            self.__cost = value
        else:
            raise ValueError('Стоимость не может быть отрицательной.')

    def __str__(self) -> str:
        return f'{self.__name}, {self.__store}, {self.__cost}р.'

    def __add__(self, other):
        return self.__cost + other.__cost


class Warehouse:
    def __init__(self, *products: Product) -> None:
        self.__list_of_products = list(products)

    @property
    def list_of_products(self):
        return self.__list_of_products

    def __getitem__(self, i: int) -> None:
        if i >= len(self.__list_of_products) or i < 0:
            print('Товар не найден.')
        else:
            print(self.__list_of_products[i])

    def find_product(self, name: str) -> None:
        is_product: bool = False

        for product in self.__list_of_products:
            if product.name == name:
                is_product = True
                print(product)

        if not is_product:
            print('Товары не найдены.')

    def sort_products(self, key: Callable[[Product], str | float]) -> None:
        sorted_products: list[Product] = sorted(self.__list_of_products, key=key)

        for item in sorted_products:
            print(f'[{item}]', end='; ')
        print()

    def sort_by_name(self) -> None:
        self.sort_products(lambda product: product.name)

    def sort_by_store(self) -> None:
        self.sort_products(lambda product: product.store)

    def sort_by_cost(self) -> None:
        self.sort_products(lambda product: product.cost)


pen: Product = Product('Ручка', 'Леонардо', 1.45)
pencil: Product = Product('Карандаш', 'Арт-территория', 1.6)
pencil1: Product = Product('Карандаш', 'Три цены', 1.4)
my_warehouse: Warehouse = Warehouse(pen, pencil, pencil1)

print(pen + pencil)

my_warehouse[2]
my_warehouse.find_product('Карандаш')

my_warehouse.sort_by_name()
my_warehouse.sort_by_cost()
my_warehouse.sort_by_store()
