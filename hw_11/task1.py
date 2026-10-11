class Soda:
    def __init__(self, taste: str  = '') -> None:
        self._taste: str = taste.lower()

    def __str__(self) -> str:
        if self._taste:
            return f'У вашей газировки вкус: {self._taste}'
        else:
            return 'У вас обычная газировка'


cola: Soda = Soda('Ванильный')
soda: Soda = Soda()
print(cola)
print(soda)
