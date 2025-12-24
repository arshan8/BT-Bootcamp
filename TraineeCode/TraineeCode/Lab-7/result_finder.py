class ResultFinder:
    def __init__(self):
        self._marks1 = 0
        self._marks2 = 0
        self._marks3 = 0

    # Getters & Setters
    @property
    def marks1(self):
        return self._marks1

    @marks1.setter
    def marks1(self, value):
        try:
            self._marks1 = int(value)
        except:
            raise ValueError("only Numbers allowed")

    @property
    def marks2(self):
        return self._marks2

    @marks2.setter
    def marks2(self, value):
        self._marks2 = value

    @property
    def marks3(self):
        return self._marks3

    @marks3.setter
    def marks3(self, value):
        self._marks3 = value

    # Display marks using getters
    def display_marks(self):
        print("Marks 1 :", self.marks1)
        print("Marks 2 :", self.marks2)
        print("Marks 3 :", self.marks3)

    # Derived values → calculated, not stored
    def get_total(self):
        return self.marks1 + self.marks2 + self.marks3

    def get_average(self):
        return self.get_total() / 3

    def get_result(self):
        if self.marks1 >= 40 and self.marks2 >= 40 and self.marks3 >= 40:
            return "PASS"
        else:
            return "FAIL"
