"""first_name = input("Enter your first name")
Last_name = input("Enter your last name")
age = int(input("Enter your age"))

if age < 18:
    print('You are a minor')
elif age > 18 and age < 50:
    print(f'{first_name} {Last_name}, with {age}, you are an adult')
else:
    print('You are a retiry')

    
prompt = "Enter your to do lists: "
prompt_list = []

while True:
    todo = input(prompt)
    printed_todo = todo.capitalize()
    prompt_list.append(printed_todo)
    print(prompt_list)
    length = len(todo)
    print(f"The length of your prompt is: {length}")
    if length < 4:
        print("It's long character")
    elif (length > 4 and length < 20):
        print("It medium size")
    else:
        print("It is too long")
        
customer = { "first_name": "Bikila", "last_name": "Tolessa", "age": 30    
}
keys = customer.keys()
values = customer.values()
print(f'the keys are as follows:')
for k in keys:
    
    print(k)
print(f'the values are as follow:')
for v in values:
    
    print(v)"""

""" import pandas as pd

people = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'Chicago'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]

news = pd.DataFrame(people)
ages = news['age']
age_listed = list(ages)
sum_age = 0
print(ages)
print(age_listed)

for a in age_listed:
    sum_age = sum_age + a
print(f'The total sum of ages is {sum_age}') """

"""
new_record = pd.read_csv('employees.csv')
new_record.sort_values(by='Team')
print(new_record) 


def funct1():
    print("You are awesome")
funct1()

def funct2(arg1, arg2):
    sum = arg1 * arg2
    return sum
funct2(4, 4)
print(funct2(4, 4)) 

sum = 0
for i in range(0, 20):
    if i % 2 == 0:
        sum = sum + i
print(sum)


def evn_or_odd():
    max_try = 0
    while max_try <= 5:
        val = int(input("Enter a number"))
        max_try = max_try + 1
        if val % 2 == 0:
            print(f'This is an even number')
        else:
            print(f'It is an odd number')
    else:
        print(f'You have exceeded the max')


evn_or_odd()"""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def honk(self):
        print(f'We honk honk')
    def accelarate(self):
        print(f'{self.model} cars are so fast')
honda = Car('Honda', 'SUV', 1990)
honda.honk()
honda.accelarate()

