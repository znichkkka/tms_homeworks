class Bus:
    def __init__(
        self,
        max_num_of_seats: int,
        max_speed: int | float,
    ) -> None:
        self.max_num_of_seats = max_num_of_seats
        self.max_speed = max_speed
        self.speed: int | float = 0
        self.surnames: list[str] = []
        self.seats: dict[int, str] = {seat: '' for seat in range(1, max_num_of_seats + 1)}

    @property
    def is_free_seat(self) -> bool:
        for s in self.seats.values():
            if s == '':
                return True
        return False

    def __str__(self) -> str:
        return f'Места: {self.seats}, {self.speed} км/ч, max = {self.max_speed} км/ч, свободные места: {self.is_free_seat}'

    def drop_off_passenger(self, *surnames: str) -> None:
        for current_surname in surnames:
            for seat, surname in self.seats.items():
                if current_surname == surname:
                    self.seats[seat] = ''
                    if current_surname in self.surnames:
                        self.surnames.remove(current_surname)
                    break

    def __isub__(self, other: str) -> 'Bus':
        self.drop_off_passenger(other)
        return self

    def pick_up_passenger(self, *surnames: str) -> None:
        for current_surname in surnames:
            if not self.is_free_seat:
                print('Свободных мест нету.')
                return

            for seat, surname in self.seats.items():
                    if not surname:
                        self.seats[seat] = current_surname
                        self.surnames.append(current_surname)
                        break

    def __iadd__(self, other: str) -> 'Bus':
        self.pick_up_passenger(other)
        return self

    def increase_speed(self, num: int | float) -> int | float:
        if num < 0:
            raise ValueError('Передаваемое значение не может быть отрицательным.')
        if self.speed + num <= self.max_speed:
            self.speed += num
        else:
            print('Нельзя превысить максимальную скорость.')
        return self.speed

    def decrease_speed(self, num: int | float) -> int | float:
        if num < 0:
            raise ValueError('Передаваемое значение не может быть отрицательным.')
        if self.speed >= num:
            self.speed -= num
        else:
            print('Скорость не может быть ниже ноля.')
        return self.speed

    def __contains__(self, item: str) -> bool:
        return item in self.surnames


first_bus: Bus = Bus(15, 140)
second_bus: Bus = Bus(20, 120)

print(first_bus.increase_speed(30))
print(second_bus.increase_speed(60))
print(second_bus.decrease_speed(10))

first_bus.pick_up_passenger('Petrova', 'Niva')
first_bus += 'Ivanova'
first_bus.drop_off_passenger('Niva')
print(first_bus)
print(first_bus.is_free_seat)

print(second_bus)

print('Ivanova' in first_bus.surnames)
