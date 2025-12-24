class DecimalSplitter:
    """
    Method to get the whole number from a double
    """
    @staticmethod   #called directly on class, so staticmethod is needed, because its not bound to object instace, might work but breaks if bymistakely called on object
    def get_whole(number):
        return int(number)

    """
    Method to get the fractional part of a double number
    """
    @staticmethod
    def get_fraction(number):
        return round(number - int(number),2)

    """
    Method to check if a given number is odd or even
    """

    @staticmethod
    def is_odd(number):
        return int(number) & 1
