import datetime

print('Hi this is a homework questionnaire. Answer a couple of questions')
first_name = input('Enter your first name ')
last_name = input('Enter your last name ')
print('welcome', first_name, last_name, 'there are still a couple of questions')
from datetime import date, timedelta

print('enter your date of birth')
year = int(input('Enter a year '))
month = int(input('Enter a month '))
day = int(input('Enter a day '))
date_of_birth = datetime.date(year, month, day)
age = (date.today() - date_of_birth)
print('you are already ', age)  # тут у меня настал ступор изначально хотел через datetime.date(input()), но пришлось пойти таким путем и то получились дни (
survey = int(input('why did you consider taking courses choose answer option\n 1 work in science\n 2 much money\n 3work at home and code\n'))
if survey == 1:
    print('I see you are a scientist')
elif survey == 2:
    print('for this you need to work')
elif survey == 3:
    print('you still have to go to the office to drink coffee')
else:
    print('there are only 3 options')
print('this was the first homework',first_name,last_name,'see you again. And dont forget beautiful is better than ugly')
