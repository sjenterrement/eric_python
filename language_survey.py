from survey import AnonymousSurvey

#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question ="What language did you first learn to speak?"
my_survey=AnonymousSurvey(question)

#先是问题并存储问题
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response=input("Language: ")
    if response=='q':
        break;
    my_survey.store_response(response)

#显示调查结果
print("\nThank you to everyone who articipated in the survey!")
my_survey.show_results() 