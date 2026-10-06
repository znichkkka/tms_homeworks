class Math:
    def addition(self, num1, num2) -> float:
        return num1 + num2

    def subtraction(self, num1, num2) -> float:
        return num1 - num2

    def multiplication(self, num1, num2) -> float:
        return num1 * num2

    def division(self, num1, num2) -> float:
        return num1 / num2

operation: Math = Math()
print(operation.addition(3, 8))
print(operation.subtraction(3, 8))
print(operation.multiplication(3, 8))
print(operation.division(16, 8))