x1 = 1
x2 = 2
x3 = 3
x = 1.7


x_arr = [x1,x2,x3]
x2 = x
x_arr.sort()
for i, x_e in enumerate(x_arr):
    if x_e > x2:
        x1 = x_arr[i-1]
        x3 = x_e
        break
print(x1, x2, x3)
