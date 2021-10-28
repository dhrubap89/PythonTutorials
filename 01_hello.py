'''import os
print("Hello World")#Hello  world   prog

####    chapter 1

#   print type of variables
a=25
b=2.9
c="Dhruba"
d=True
e=None
print('Type of a :', type(a))
print('Type of b :', type(b))
print('Type of c :', type(c))
print('Type of d :', type(d))
print('Type of e :', type(e))

####    chapter 2
a=input("Enter a number:    ")
b=input("Enter another number:  ")
a=int(a)
b=int(b)
print("a is greater than b:",a>b)
#c=a+b
c=a%b
print('a % b:',c)
print('average of a and b is:',(a+b)/2)
print('square of a and b is:',pow(a,2),pow(b,2))


####    chapter 3
name="Dhruba Ratan Paul"

print('characters from 0 upto index 4 are:',name[0:])    # characters from index 0 to 3  similar to  name[:4]
print('characters from start upto index -1 are:',name[:-1])
print('characters from index -5 upto last index skiping 2:',name[-6::2])

print('length of name string:',len(name))
print(name.endswith('ba'))
print(name.capitalize())
print(name.count('a'))
print(name.find('ata'))
print(name.replace('ata','xtx'))


#chapter 3  prob1
greeting=", Good Afternoon"
name=input("Enter your name: ")
print(name,greeting)


#chapter 3  prob2
name    =   input("Enter your name: ")
date    =   input("Enter today's date: ")
letter= '''
# \nDear   <|NAME|>
# You are Selected

# Date:  <|DATE|>
'''
letter=letter.replace("<|NAME|>",name)#must have to copy result to a variable
letter=letter.replace("<|DATE|>",date)

print(letter)


# chapter 4   List
#List is ordered container which can hold multiple  datatypes
a=[1,2,4,'Dhruba',5,66,78,True,None,45]
print(a)

#list slicing
friends=['Harry','Tom','Rohan','Arup','Divya',45]
print(friends[0:4])

#list functions/methods
l1=[1,34,22,11,49,67]
print(l1)
l1.sort()#sort the  list
print(l1)
l1.reverse()#reverse the list
print(l1)
l1.append(45)#append the item at the end of the list
print(l1)
l1.insert(1,347)#inserts 347  at the position index 1 of the list
print(l1)
l1.pop(1)#remove element at index 1
print(l1)
l1.remove(45)#remove the item of value  45
print(l1)

#tuples
#creating a tuple  using   parentheses
t=(1,2,4,5)
t1=()#empty tuple
t1=(1,)#tuple with  single  element
#t1=(1)#wrong   way

#can not update(immutable) the items of tuples

#tuple  methods
t=(1,2,4,5)
print(t)
print(t.count(1))
print(t.index(1))



#practice  list/tuples

#store items from  user input   -problem 1
f1=input("Enter fruit number 1:")
f2=input("Enter fruit number 2:")
f3=input("Enter fruit number 3:")
f4=input("Enter fruit number 4:")
f5=input("Enter fruit number 5:")
f6=input("Enter fruit number 6:")
f7=input("Enter fruit number 7:")

myFruitList= [f1,f2,f3,f4,f5,f6,f7]

print(myFruitList)

#problem    2
m1=input("Enter marks for student number 1:")
m2=input("Enter marks for student number 2:")
m3=input("Enter marks for student number 3:")
m4=input("Enter marks for student number 4:")
m5=input("Enter marks for student number 5:")
m6=input("Enter marks for student number 6:")
m7=input("Enter marks for student number 7:")

myList=[m1,m2,m3,m4,m5,m6,m7]
myList.sort()
print(myList)


#problem 4
a=[1,45,34,21]
print(a[0]+a[1]+a[2]+a[3])
print(sum(a))

a=[7,0,8,9,0,10]
print(a.count(0))


#Dictionary &   Sets
myDict = {
    "Fast" : "In a quick manner",
    "Dhruba" : "A coder",
    "marks" : [1,2,5],
    "anotherDict" : {'Dhruba':'player'}
}

# print(myDict["Fast"])
# print(myDict["marks"])
# myDict["marks"]=[45,79,98]
# print(myDict["marks"])

# print(myDict["anotherDict"]['Dhruba'])

#dictionary methods
print(myDict.keys())
print(myDict.values())
print(myDict.items())

updateDict={
    "lovish":"friend",
    "robin":"friend",
    "bina":"friend",
    "Dhruba":"A Cricketer"


}
myDict.update(updateDict)
print(myDict.items())
print(myDict.get("Dhruba2"))#if key not present returns none
print(myDict["Dhruba2"])#throws error   if  key not present

#sets in python
a={1,4,7,1}
print(a)
print(type(a))

a={}#Important: is  an  empty Dictionary,   not an  empty   set
print(type(a))


b=set()#creates an  empty   set
print(type(b))
b.add(4)
b.add(7)
b.add(4)
#b.add([4,5,6])#can not add list/Dict in a set, because list/Dict is not hashable
b.add((4,5,6))
print(b)
print(len(b))
b.remove(4)#remove 4 from Set b
print(b)
print(b.pop())#pop function removes random element from Set
print(b)

#create a dictionary to collect favorite languages from 4 friends
favLang={}
a=input("Enter your favorite language Saikat\n")
b=input("Enter your favorite language Arup\n")
c=input("Enter your favorite language Dhiman\n")
d=input("Enter your favorite language Suhel\n")
favLang['Saikat']=a
favLang['Arup']=b
favLang['Dhiman']=c
favLang['Suhel']=d
print(favLang)


#Conditional Expressions in Python
a=int(input("ENter Your AGe:\n"))
if a>=18:
    print("Yes")
else:
    print("No")


#problem
m1=int(input("Enter mark for Subject1:\n"))
m2=int(input("Enter mark for Subject2:\n"))
m3=int(input("Enter mark for Subject3:\n"))
total=m1+m2+m3
total_prcnt=(total/300)*100
if m1>=33 and m2>=33 and m3>=33 and total_prcnt>=40:
    print("Pass")
else:
    print("Fail")

#problem
post=input("Enter the string you want to post:\n")
print(post)
post=post.lower()
print(post)

if 'harry' in post:
    print("The post is about harry")
else:
    print("The post is not about harry")



#loops in Python
fruits = ['Banana', 'Watermelon', 'Grapes', 'Apple', 'Orange']
#i = 0

# while i < len(fruits):
#     print(fruits[i])
#     i=i+1
for item in fruits:
    print(item)


#problem - multiplication table using for loop
number = int(input("Enter a number: \n"))

for i in range(1,11):
    if i==1:
        print()

    #result=i*number
    #print(str(number) + " * " + str(i) + " = " + str(number*1))
    print(f"{number}X{i}={number*i}")#f string
else:
    print("\nDone!!!")

#problem
l1=["Harry", "Soham", "Sachin", "Rahul"]

for name in l1:
    if name.lower().startswith("s"):
        print("Hello " + name)
#problem - prime number
number = int(input("Enter a number: \n"))

prime = True

for i in range(2, number):
    if number%i == 0:
        prime = False
if prime:
    print(str(number) + " is a prime number!")
else:
    print(str(number) + " is not a prime number!")


#problem - find sum of first n natural numbers
number = int(input("Enter a number: \n"))
i=0
result=0

while i<number:
    result=result+i
    i=i+1

print("Sum of first "+ str(number)+ " natural numbers is: " + str(result))

# problem - factorial of a given number
number = int(input("Enter a number: \n"))
fact=1

for i in range(1,number+1):
    fact=fact*i

print(f"The factorial of {number} is {fact}")



#problem - star pattern
n=3

for i in range(4):
    print("*" * i)



#functions
def greet(name="stranger"):#function with default parameter
    print("Hello, "+name)

greet("Harry")
greet()



def factorial(num):
    product=1
    for i in range(num):
        product=product*(i+1)
    return product

def factorial_recursive(num):
    if num == 1 or num == 0:
        return 1
    else:
        return  num * factorial_recursive(num-1)

print(factorial(5))
print(factorial_recursive(5))
print(factorial_recursive(0))

#problem - 1 Find greatest of 3 numbers
def greatest(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3 and n2 > n1:
        return n2
    else:
        return n3

def farh(cel):
    return  cel*(9/5)+32

print(greatest(49,35,48))
print(farh(105),end="")

def sum_rec(n):
    if n<=1:
        return 1
    else:
        return n + sum_rec(n-1)

print(sum_rec(6))

n=3
for i in range(n):
    print("*" * (n-i))



def remove_and_strip(str, word):
    newStr = str.replace(word,"")
    return newStr.strip()

test_str = "    Dhruba is a good boy   "
n = remove_and_strip(test_str,"Dhruba")
print(n)
#print(test_str.strip())


#project 1 - Snake Water Gun GAME
import random

def game_result(comp, you):
    if  comp == you:
        return None
    elif comp == 's':
        if  you == 'g':
            return True
        elif you == 'w':
            return False
    elif comp == 'g':
        if  you == 'w':
            return True
        elif you == 's':
            return False
    elif comp == 'w':
        if  you == 's':
            return True
        elif you == 'g':
            return False


print("Computer Turn: Choose Snake(s), Water(w) or Gun(g) \n")
randNo = random.randint(1,3)
if  randNo == 1:
    comp = 's'
elif    randNo == 2:
    comp = 'w'
elif    randNo == 3:
    comp = 'g'

print("Your's Turn: Choose Snake(s), Water(w) or Gun(g) \n")
you = input("Enter your choice: \n")
print(f"Computer Chose: {comp}")
print(f"You Chose: {you}")

result = game_result(comp, you)
if  result == None:
    print("The Game is a Tie!")
elif result == True:
    print("You Win!")
else:
    print("You Lose!")


#File operation in Python
# f = open('sample.txt', 'r')
f = open('sample.txt') # by default the mode is r(read)

data = f.read()
print(data)
f.close()
#write files in python r- read, w-write, a-append, +-update(works only with other mode and makes file able to read and write together)
f=open('sample.txt', 'a+')
f.write("\nThis Line is updated by Python")
data1 = f.read()
print(data1)
f.close()


# with open('another.txt', 'w+') as f:#using with open method we can avoid using f.close() function
#     f.write("Creatd by Python using 'with open' method \n")
with open('another.txt', 'r+') as f:#using with open method we can avoid using f.close() function
    a=f.read()
    print(a)


#problem
with open('poems.txt') as f:
    data = f.read()

if 'twinkle' in data:
    print("Twinkle is Present")
else:
    print("Twinkle is not Present")


#problem
def game():
    return 69

score = game()
with open ("hiscore.txt") as f:
    hiScoreStr = f.read()

if hiScoreStr == '':
    with open ("hiscore.txt", "w") as f:
        f.write(str(score))
elif int(hiScoreStr) < score:
    with open ("hiscore.txt", "w") as f:
        f.write(str(score))

#problem - multiplication tables

for i in range (2,21):
    with open(f"tables/{i}.txt", "w") as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")

#problem - read line number from a log
content = True
i = 1

with open("logfile.txt") as f:
    while content:
        content = f.readline().lower()
        if  "python" in content:
            print(content)
            print(f"'python' is found in Line No:{i}")
        # else:
        #     print("Python is not present in log")
        i+=1

#problem - wipe out the contents of a file
with open("hiscore.txt", 'w') as f:
    f.write("")


import os

os.remove("sample2.txt")#to delete a file


#oops in python
#practice problems

#problem 1
from os import name


class Programmer:
    company = "Microsoft"

    def __init__(self, name, product) -> None:
        self.name = name
        self.product = product
    
    def getInfo(self):
        print(f"Employee {self.name} works in the product {self.product}")

harry = Programmer("Harry", "GitHub")
alka = Programmer("Alka", "Skype")

harry.getInfo()
alka.getInfo()


#problem

class Calculator:

    def __init__(self, num) -> None:
        self.number = num

    def square(self):
        print(f"The square of the number {self.number} is {pow(self.number, 2)}")

    def cube(self):
        print(f"The cube of the number {self.number} is {pow(self.number, 3)}")
    
    def squareRoot(self):
        print(f"The square root of the number {self.number} is {pow(self.number, 0.5)}")
    
    @staticmethod
    def greet():
        print(">>>>Hello User, Welcome to the Calculator Program!<<<<")


a = Calculator(9)
a.greet()
a.square()
a.cube()
a.squareRoot()

#problem
from random import sample


class Sample:
    a = "Harry"

obj = Sample()
obj.a = "Vicky" # does not change class atttribute, adding instance attribute
#Sample.a= "Vicky" # to change class attribute

print(Sample.a)
print(obj.a)


#problem 
class Train:

    def __init__(self, name, fare, seats) -> None:
        print("*** Welcome to Indian Railways ***")
        self.name = name
        self.fare = fare
        self.seats = seats

    def bookTicket(self):
        if (self.seats > 0):
            print(f"Congrats, your ticket has been booked, seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, this train is full. Kindly try in Tatkal")

    def getStatus(self):
        print(f"*****The name of the Train is {self.name}")
        print(f"The seats available of the Train is {self.seats}")

    def getFareInfo(self):
        print(f"The price of the ticket is Rs. {self.fare}")

intercity = Train("Intercity Express (23015)", 150, 2)
intercity.getFareInfo()

intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()



#Single inheritance in Python
class Employee:
    company = "Google"
    def showDetails(self):
        print("This is an Employee")

class Programmer(Employee):
    language = "Python"
    def showDetails(self):#override base class function
        print("This is an Programmer")

e=Employee()
e.showDetails()
p=Programmer()
p.showDetails()


# multiple Inheritance

class Employee:
    company = "Visa"
    ecode = 129

class Freelancer:
    company = "FiverR"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer): # multiple inheritance sequence - prioritize first base class
    name = "Rohit"

p = Programmer()
print(p.company) # Visa - as Employee is 1st base class

# In multilevel inheritance value of latest parent will be produced, if function is common is multilevel base

# @staticmethod - is used to make a class method static. Usually static functions are made when no class properties to be used
# @classmethod  - is used to change value of class instances/properties (values) directly
# super() - is used to access methods of a super/base class

# property decorators/ @getter/@setter methods
class employee:
    company = "IOCL"
    salary = 5600
    salaryBonus = 500

    @property                   #@property methods are called as getter methods
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary


e = employee()
print(e.salary)
print(e.salaryBonus)
print(e.totalSalary)    # totalSalary method is acting as a class property
e.totalSalary = 5800    # totalSalary setter method is setting the new salaryBonus value
print(e.salary)
print(e.salaryBonus)


# operator overloading in python

class Number:
    def __init__(self, num) -> None:
        self.num = num

    def __add__(self, num2):    #operator overloading
        print("Lets Add..")
        return self.num + num2.num

    def __mul__(self, num2):    #operator overloading
        print("Lets Multiply..")
        return self.num * num2.num

    def __str__(self) -> str:   #other dunder methods in python
        return f"Decimal Number: {self.num}"

    def __len__(self):          #other dunder methods in python
        return len(str(self.num))

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
print(sum)
mul = n1 * n2
print(mul)
print(n1)
print(len(n1))


#inheritance problems

#problem - create 3d vector class using 2d vector class

class  C2dVec:
    def __init__(self, i, j) -> None:
        self.icap = i
        self.jcap = j

    def __str__(self) -> str:
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i, j, k) -> None:
        super().__init__(i, j)
        self.kcap = k

    def __str__(self) -> str:
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVec(1,7)
v3d = C3dVec(3, 9, 5)

print(v2d)
print(v3d)



#problem 2

class  Animals:
    def __init__(self, name) -> None:
        print(f"{name} is an Animal")

class   Pets(Animals):
    def __init__(self, name) -> None:
        super().__init__(name)
        print(f"{name} is a Pet")

class   Dogs(Pets):
    def __init__(self, name) -> None:
        super().__init__(name)
        print(f"{name} is a Dog")

    @staticmethod
    def bark():
        print("Bow bow!!!")

tiger = Animals("Tiger")
cat = Pets("Cat")
dog = Dogs("Dog")
dog.bark()


#problem 3

class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)

e.salaryAfterIncrement = 2000
print(e.increment)

#problem - complex number

class ComplexNumber:
    def __init__(self, r, i) -> None:
        self.real = r
        self.imag = i

    def __str__(self) -> str:
        return f"The Complex number is: {self.real} + {self.imag}i"

    def __add__(self, num2):
        print("Lets add 2 complex numbers")
        return ComplexNumber(self.real + num2.real, self.imag + num2.imag)

    def __mul__(self, num2):
        print("Lets multiply 2 complex numbers")

        # (a+bi)(c+di) = (ac−bd) + (ad+bc)i

        mulReal = self.real * num2.real - self.imag * num2.imag
        mulImag = self.real * num2.imag + self.imag * num2.real

        return ComplexNumber(mulReal, mulImag)

c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)
sum = c1 + c2
print(str(sum))
mul = c1 * c2
print(str(mul))

#problem - Sum and dot product of a vector
class Vector():
    def __init__(self, vec) -> None:
        self.vec = vec
    
    def __str__(self) -> str:
        # str1 = ""
        # cnt = 0
        # for i in self.vec:
        #     str1 += f" {i} V{cnt} "
        #     cnt += 1
        # return str1[:-1]
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
    
    def __add__(self, v2):       # u→= ⟨u1,u2⟩ and v→ = ⟨v1,v2⟩,  => u→ + v→ =⟨u1+v1 , u2+v2⟩
        if  len(self.vec) != len(v2.vec):
            return f"Error! Vectors length/dimensions are not same"

        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + v2.vec[i])
        return  Vector(newList)

    def __mul__(self, v2):
        if  len(self.vec) != len(v2.vec):
            return f"Error! Vectors length/dimensions are not same"
        
        mul = 0
        for i in range(len(self.vec)):
            mul += self.vec[i] * v2.vec[i]  #u ⋅ v = u1v1 + u2v2 + u3v3 + ... + uNvN
        return  mul

    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 4, 6, 7])
v2 = Vector([1, 6, 9])

print(f"v1: {str(v1)}")
print(f"v2: {str(v2)}")
print(f"Length of v1: {len(v1)}")
print(f"Length of v1: {len(v2)}")
sum=v1+v2
print(f"Addition of 2 vectors: {sum}")
mul=v1*v2
print(f"Product of 2 vectors: {mul}")

#Project 2 - Guess a number
import random

randomNum = random.randint(1, 100)
# print(randomNum)
userGuess = None
guesses = 0
while (userGuess != randomNum):
    print("Enter 'q' to Quit!")
    
    userGuess = input("Guess a Number from 1 to 100:\n")
    if  userGuess == 'q':
        break

    try:
        userGuess = int(userGuess)
        guesses += 1

        if (userGuess == randomNum):
            print("You guessed it Right!")
            break
        else:
            if (userGuess > randomNum):
                print("You guessed it Wrong! Please enter a smaller Number")
            else:
                print("You guessed it Wrong! Please enter a larger Number")
    
    except  Exception as e:
        print(f"Your input resulted in an error.\n{e}")

if guesses > 0:
    print(f"You guessed it in {guesses} attempts")

    with open('hiscore.txt') as f:
        hiscore = f.read().strip()

    if  len(hiscore) == 0:
        hiscore = 0
    else:
        hiscore = int(hiscore)

    if guesses < hiscore:
        print("Congrats! You just beat the Highest score")

        with open('hiscore.txt', "w") as f:
            f.write(str(guesses))


# ENumerate Function
List1 = [1,5,7,9,45,67,98]
for i,item in enumerate(List1):
    print(i, item)


#List Comprehension
List1 = [1,5,7,9,45,67,98]
List2 = [item for item in List1 if item>10]
print(List2)


#Advance Python - Chapter 1 practice problem

#problem 1

def readFile(fname):
    try:
        with open(fname) as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"file: {fname} is not found")

readFile("1.txt")
readFile("poems.txt")
readFile("hiscore.txt")

#problem 2
List1 = [1,4,7,9,15,78,56,46]
for i,item in enumerate(List1):
    if  i==2 or i==4 or i==6:
        print(f"Index:{i+1} element is: {item}")


#problem 3
while True:
    try:
        num = input("ENter a number: ")
        f_num = int(num)
        List1 = [f_num*item for item in range(1,11)]
        print(List1)
        break
    except ValueError as e:
        print(f"You entered: {num} is not a number! Please enter a valid number")


#problem 4
a=int(input("Enter a number: "))
print(a)
b=int(input("Enter another number: "))
print(b)
try:
    div = a/b
    print(div)
except ZeroDivisionError as e:
    print("Result is infinity!")

#lambda Functions
square = lambda x : x*x
sum = lambda a,b,c : a+b+c

num = 6
print(square(num))
print(sum(num, 4, 7))

#join method
list1 = ["apple", "samsung", "motorola", "nokia", "one plus", "oppo", "vivo", "poco"]
# sentence = " | ".join(list1)
sentence = " , ".join(list1)
print(sentence)


#format method
name = "Dhruba"
channel = "Bla bla"
type= "coding"
str = "This is {0} and his {2} channel is {1}".format(name, channel, type)
print(str)

# map method
def square(x):
    return x*x
# Syntax: list(map(function,list))
list1 = [1, 4, 7]
print(list(map(square,list1)))  #mapping square function with the list

# filter method
# Syntax: list(filter(function,list))

def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False
gt_5 = lambda num : num > 5

list1 = [1,2,5,7,9,45,23,59,70]

print(list(filter(gt_5,list1)))

# reduce method
from functools import reduce

sum = lambda a,b : a+b

list1=[1,2,3,4]
list_sum = reduce(sum,list1)
print(list_sum)


#chapter 13 - Practice

#problem 1
# pip install virtualenv                -> to install virtual environment packages in python
# virtualenv myprojectenv               -> to create a virtual environment named myprojectenv
# .\myprojectenv\Scripts\activate.ps1   -> activate the new virtual env and switch to that env
# pip install package_name              -> install the desired package to that env
# pip freeze > rqmt.txt                 -> create the package list installed in the environment and copy those to a file named "rqmt.txt"
# deactivate                            -> logout from the previous environment
# virtualenv myprojectenv2              -> to create another virtual environment named myprojectenv2
# pip install -r .\rqmt.txt             -> install list of packages recursively as listed in rqmt.txt file in new env

# problem 2
name = input("Enter your Name: ")
marks = int(input("Enter your marks: "))
phn = input("Enter your phone number: ")

sentence = "The name of the student is {0}, his marks are {1} and phone number is {2}".format(name, marks, phn)
print(sentence)


#problem 3
list1 = [str(i*7) for i in range(1,11)]
ver_list = "\n".join(list1)
print(ver_list)

#problem 4
div_by_5_lambda = lambda num : num%5 == 0

list1 = [1,5,7,9,15,21,25,32,35]
print(list(filter(div_by_5_lambda,list1)))

#problem 5
from functools import reduce

list1 = [4,2,5,19,10,25]
val = reduce(max,list1)
print(val)
'''

#project 3
#library management system
class Library:
    def __init__(self,booklist) -> None:
        self.books = booklist
    def borrowBook(self, book):
        if book in self.books:
            print(f"Congrats! You have been issued the book: {book}")
            self.books.remove(book)
        else:
            print("Sorry this book is not available!")

    def returnBook(self, book):
        print(f"Thanks for donating/returning the book: {book}. Hope you enjoyed it.")
        self.books.append(book)

    def listAllBooks(self):
        print("The list of available books are: ")
        for i,book in enumerate(self.books):
            print(f"{i+1}. {book}")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the Book to be requested: ")
        return self.book
    def returnBook(self):
        self.book = input("Enter the name of the Book to be returned: ")
        return self.book

if __name__ == "__main__":
    l1 = Library(["Algorithms", "Python", "Django", "Data Structure", "C++"])
    s1 = Student()
    welcomeMsg = '''\n=====  Welcome to the Dhruba's Library  =====
    The available options are:
        1. Display All Books
        2. Request a Book
        3. Return/Donate a Book
        4. Exit the Library
    '''
    while (True):
        print(welcomeMsg)
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            l1.listAllBooks()
        elif choice == 2:
            l1.borrowBook(s1.requestBook())
        elif choice == 3:
            l1.returnBook(s1.returnBook())
        elif choice == 4:
            exit()
        else:
            print("Invalid Choice!")

print("Thanks for visiting the Dhruba's Library!")

