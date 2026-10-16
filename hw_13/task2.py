from typing import Generator


def create_loop_sequence(amount: int) -> Generator[int]:
    if amount < 0:
        raise ValueError('Количество не может отрицательным числом.')

    count: int = 0
    while count <= amount:
        for num in range(1, 4):
            count += 1
            if count <= amount:
                yield num


if __name__ == '__main__':
    try:
        amount_of_num: int = int(input('Количество чисел для вывода: '))
        for i in create_loop_sequence(amount_of_num):
            print(i, end=' ')
    except ValueError as e:
        print(f'Ошибка: {e}')
