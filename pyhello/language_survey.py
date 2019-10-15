from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question="what language did you first learn to speak?"
my_survey=AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("enter 'q' at any time to quit.\n")

while True:
    response=input("language: ")
    if response=='q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("\nthank you to everyone who participated in the survey")
my_survey.show_results()