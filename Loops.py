#for loop
from operator import truediv

for i in range(0,6):
    print(i)
print("For loop is over")

#while loop
birthday_month=input("Enter your birthday month")
var=True
while var==True:
    if birthday_month=='5':
        print("That right")
        break
    else :
        print("Better luck next time")
        var=False
print("While loop is over")

#List
fruits=["apple", "orange", "mango", "banana", "litchi"]
print("this is first element in the list....", fruits[0])
print("Interesting order in the list...", fruits[-5],'and',fruits[-3])
print("No. of fruits till now",len(fruits))
fruits.append("papaya")
print("New list..")
for item in fruits:
    print(item,"\n")
    
fruits.pop(0)
fruits.remove("mango")
print("after removing fruits from the list")
for item in fruits:
    print(item,"\n")
    
fruits.sort()
print("See the sorted fruits list now",fruits)
print("what is the first item in the list..",fruits[0])
    




