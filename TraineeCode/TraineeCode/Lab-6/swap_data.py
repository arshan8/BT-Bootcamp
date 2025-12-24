class SwapData:
    """
    Properties of the class
    """
    def __init__(self):
        self._number1 = 0
        self._number2 = 0

    # for number1
    @property
    def number1(self):
        return self._number1

    @number1.setter
    def number1(self, value):
        try:
            self._number1 = int(value)
        except:
            raise ValueError("Only Integers allowed")

    # for number2
    @property
    def number2(self):
        return self._number2

    @number2.setter
    def number2(self, value):
        try:
            self._number2 = int(value)
        except:
            raise ValueError("Only Integers allowed")


    def swap_values(self):
        """swap values"""
       
        self._number1 = self._number2 ^ self._number1
        self._number2 = self._number2 ^ self._number1
        self._number1 = self._number2 ^ self._number1

    """
    Method to display the numbers before and after swapping
    """
    def display_values(self, str_msg):
        print(str_msg)
        print("Number 1 = " + str(self._number1))
        print("Number 2 = " + str(self._number2))
