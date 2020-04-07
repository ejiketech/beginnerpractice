import datetime

u_name = input("Please kindly enter your name: ")
u_age = int(input("How old are you? "))
x = 100 - u_age

# x is the number of years to 100

this_year = datetime.datetime.now()
this_year = this_year.year
yearto100 = this_year + x
msg = f'Hello {u_name} you will be 100 years old in the year {yearto100}'
print(msg)


