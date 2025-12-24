"""the design follows the Single responsibility principle"""


# (e.g., 2 marks, 5 marks)
class Category:
    def __init__(self, name):
        self.name = name


# (e.g., Arrays, DBMS)
class Topic:
    def __init__(self, name):
        self.name = name



class Question:
    def __init__(self, qid, text, category, topic):
        self.qid = qid
        self.text = text
        self.category = category
        self.topic = topic


# inheritance
class MCQQuestion(Question):
    def __init__(self, qid, text, category, topic, options):
        super().__init__(qid, text, category, topic)
        self.options = options



class ParagraphQuestion(Question):
    def __init__(self, qid, text, category, topic):
        super().__init__(qid, text, category, topic)



class ExamPortal:
    def __init__(self):
        self.questions = []  #reference object

    def add_question(self, question):
        self.questions.append(question)

 
    def total_questions(self):
        return len(self.questions)


    def list_questions_by_topic(self, topic_name):
        return [q for q in self.questions if q.topic.name == topic_name]

  
    def list_questions_by_topic_and_category(self, topic_name, category_name):


        return [ q for q in self.questions if q.topic.name == topic_name and q.category.name == category_name ]
        




cat2 = Category("2 Marks")
cat5 = Category("5 Marks")

arrays = Topic("Arrays")
dbms = Topic("DBMS")


q1 = MCQQuestion(1, "What is an array?", cat2, arrays, ["Collection", "Data type"])
q2 = ParagraphQuestion(2, "Explain arrays in detail.", cat5, arrays)
q3 = MCQQuestion(3, "What is a primary key?", cat2, dbms, ["Unique", "Duplicate"])


portal = ExamPortal()
portal.add_question(q1)
portal.add_question(q2)
portal.add_question(q3)


print("Total Questions:", portal.total_questions())

print("\nQuestions on Arrays:")
for q in portal.list_questions_by_topic("Arrays"):
    print("-", q.text)

print("\nQuestions on Arrays (2 Marks):")
for q in portal.list_questions_by_topic_and_category("Arrays", "2 Marks"):
    print("-", q.text)
