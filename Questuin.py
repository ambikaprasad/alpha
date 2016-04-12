Questype=((1,'MCQ Single Correct'),(2,'MCQ multiple correct'),(3,'Group MCQ single correct'),(4,'True and false'),
(5,'Integer Type'),(6,'Matrix match'),(7,'Linked questions'),(8,'Assertion and Reasons type'),(9,'Subjective or descriptive type'),
(10,'Group (Common data) Subjective or descriptive type'))

Category Model:
  name=
Tag Model:
  name=


Question model:
  Questype =
  Question =
  category =
  Tag = m2m
  added_date =
  added_by =
  status =
  correct_answer =

option model:
  question=
  option=

QuestionUser:
  question=
  user=



