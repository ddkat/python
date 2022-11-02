from math import pow, sqrt
num1 = int(input())
num2 = int(input())

summ = num1 + num2
diff = num1 - num2
multi = num1 * num2
div = num1 / num2
floor_div = num1 // num2
mod = num1 % num2
sum_root = sqrt(pow(num1, 10) + pow(num2, 10)) 

print(summ, diff, multi, div, floor_div, mod, sum_root, sep='\n')