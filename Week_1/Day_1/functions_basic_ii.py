#1
def countdown (x):
    y = []
    for i in range(x,-1,-1):
        y.append(i)
    return y
print (countdown(5))

#2
def print_and_return(x):
    print(x[0])
    return x[1]
print_and_return([1,2])

#3
def first_plus_length(x):
    return x[0]+len(x)
print(first_plus_length([1,2,3,4,5]))

#4
def values_greater_than_second(x):
    y = []
    if len(x)<2:
        return False
    for i in range(0,len(x)):
        if x[i]>x[1]:
            y.append(x[i])
    if len(y)<2:
        return False
    print(len(y))
    return y
print(values_greater_than_second([5,2,3,2,1,4]))

#5
def length_and_value(x,y):
    z=[]
    for i in range(x):
        z.append(y)
    return z
print(length_and_value(6,2))