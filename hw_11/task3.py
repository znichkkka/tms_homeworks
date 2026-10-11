class SuperStr(str):
    def is_repeatance(self, some_str) -> bool:
        count: int = self.count(some_str)

        if some_str * count == self and self:
            return True
        else:
            return False

    def is_palindrom(self) -> bool:
        if self.lower() == self[::-1].lower():
            return True
        else:
            return False

new_str: SuperStr = SuperStr('ababA')
print(new_str.is_repeatance('ab'))
print(new_str.is_palindrom())

