pairs_number = int(input())

dec = [0,0,0,0]

x = 0
y = 0

for _i in range(pairs_number):
    
    x, y = list(input().split(" "))    

    x_great0 = int(x) > 0
    y_great0 = int(y) > 0
    xnot0 = int(x) != 0
    ynot0 = int(y) != 0
      
    #?y > 0 
    
    #mov $addr_y, ax 
    #mov 0, bx 
    
    #gte ax, bx 
    
         
    if x_great0 and y_great0:
        dec[0] += 1
    if not x_great0 and xnot0 and y_great0:
        dec[1] += 1
    if not x_great0 and xnot0 and not y_great0 and ynot0:
        dec[2] += 1
    if x_great0 and not y_great0 and ynot0:
        dec[3] += 1     
        
        
print("quarter 1:", dec[0])
print("quarter 2:", dec[1])
print("quarter 3:", dec[2])
print("quarter 4:", dec[3])



#for _ in range(dots_number):
#    coordinates = input()
#    x, y = map(int, input().split())


#for i in range(dots_number):
#    if is_1_quarter(x, y): 
#        quarter_1 += 1
#    if is_2_quarter(x, y):
#        quarter_2 += 1
#    if is_3_quarter(x, y):
#        quarter_3 += 1
#    if is_4_quarter(x, y):
#        quarter_4 += 1
    
#is_1_quarter = (x > 0) and (y > 0)
#is_2_quarter = (x < 0) and (y > 0)
#is_3_quarter = (x < 0) and (y < 0)
#is_4_quarter = (x > 0) and (y < 0)


#def is_1_quarter(x, y):
#    quarter_1 = 0
#    if (x > 0) and (y > 0):
#        quarter_1 += 1
#    return quarter_1
#
#def is_2_quarter(x, y):
#    quarter_2 = 0
#    if (x < 0) and (y > 0):
#        quarter_2 += 1
#    return quarter_2
#
#def is_3_quarter(x, y):
#    quarter_3 = 0
#    if (x < 0) and (y < 0):
#        quarter_3 += 1
#    return quarter_3
#
#def is_4_quarter(x, y):
#    quarter_4 = 0
#    if (x > 0) and (y < 0):
#        quarter_4 += 1
#    return quarter_4
    
