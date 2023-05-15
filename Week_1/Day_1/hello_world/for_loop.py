#1
for i in range(151):
    print(i)
#2
for i in range(5,1001):
    if i%5 == 0 :
        print(i)
#3
for i in range(1,101):
    if i%10 == 0 :
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)
#4
odd=0
for i in range(500000):
    if i%2 != 0:
        odd=odd+i
print(odd)
#5
for i in range(2018,i<0,-4):
    print(i)
#6
lowNum=2
highNum=9
mult=3
for i in range(lowNum,highNum+1):
    if i%mult == 0 :
        print(i)