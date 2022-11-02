#bmi - body mass index, calculator
user_mass = float(input())
user_height = float(input())

def bmi_classification(weight, height):
    bmi = weight / height ** 2
    
    if bmi < 18.5:
        print('Underweight')
    elif bmi > 25:
        print('Overweight')
    else:
        print('Optimal weight')

bmi_classification(user_mass, user_height)
