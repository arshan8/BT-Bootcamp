
class Student:

    def __init__(self, name, score1, score2, score3):

        self._validate_score(score1, score2, score3)

        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3


    def _validate_score(self,a,b,c):
        if not (0 <= a <= 100) or not (0 <= b <= 100) or not (0 <= c <= 100):
            raise ValueError("Scores must be between 0 and 100.")
        
    
    # @property
    # def score1(self):
    #     return self.score1
    
    # @score1.setter
    # def score1(self, val):
    #     self._validate_score()
    #     self.score1 = val

    # @property
    # def score2(self):
    #     return self.score3
    
    # @score1.setter
    # def score3(self, val):
    #     self._validate_score()
    #     self.scor3 = val

    # @property
    # def score3(self):
    #     return self.score1
    
    # @score1.setter
    # def score1(self, val):
    #     self._validate_score()
    #     self.score1 = val

    
    @property
    def total(self):
        return self.score1 + self.score2 + self.score3
        
    @property
    def average(self):
        return self.total/3
    
    @property
    def grade_class(self):
        if self.average >= 60:
            return 'First Class'
        elif self.average >= 50:
            return 'Second Class'   
        elif self.average >= 35:    
            return "Pass"    
        else:
            return 'Fail'  
        

if __name__ == "__main__":
    try:
        name = input("Enter student's name: ")
        score_1 = int(input("Enter score 1: "))
        score_2 = int(input("Enter score 2: "))
        score_3 = int(input("Enter score 3: "))
        
        arshan = Student(name, score_1, score_2,score_3)
        print(f"Name: {arshan.name}")
        print(f"Total Marks: {arshan.total}")
        print(f"Average Marks: {arshan.average:.2f}")

        arshan.score1 = int(input("update score 1: "))
        
        print(f"Updated Total Marks: {arshan.total}")

        # arshan.average = 1009  #will this be allowed
       

    except ValueError:
        print("Invalid input: Please enter valid scores.")