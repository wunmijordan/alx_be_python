# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Does not access class or instance attributes.
        Simply performs addition of two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Has access to the class itself via 'cls'.
        Uses the class attribute 'calculation_type' before performing multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
