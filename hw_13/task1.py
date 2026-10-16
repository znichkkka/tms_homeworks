from typing import Generator


def find_fibo(end: int) -> Generator[int]:
    if end < 1:
        raise ValueError('Передаваемое значение должно быть не меньше 1.')

    previous_num: int = 0
    cur_num: int = 1

    while previous_num <= end:
        yield previous_num
        previous_num, cur_num = cur_num, previous_num + cur_num


if __name__ == '__main__':
    try:
        end_of_fibo: int = int(input('Конец последовательности: '))
        generator: Generator[int] = find_fibo(end_of_fibo)
        for i in generator:
            print(i, end=' ')
    except ValueError as e:
        print(f'Ошибка: {e}')
