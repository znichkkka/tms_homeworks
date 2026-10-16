from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass


class AnimalFactory:
    @staticmethod
    def create_animal(kind_of_animal: str) -> Animal:
        normalize_kind: str = kind_of_animal.lower()
        if normalize_kind == 'dog':
            return Dog()
        elif normalize_kind == 'cat':
            return Cat()
        raise ValueError('Допустимо создание только кошек или собак.')


class Dog(Animal):
    def speak(self) -> str:
        return 'Гав-гав'


class Cat(Animal):
    def speak(self) -> str:
        return 'Мяу-мяу'


def main() -> None:
    for kind in ('Dog', 'cat', 'Cat', 'fish', 'dog'):
            try:
                animal: Animal = AnimalFactory.create_animal(kind)
                print(animal.speak())
            except ValueError as e:
                print(f'Ошибка: {e}')


if __name__ == '__main__':
    main()
