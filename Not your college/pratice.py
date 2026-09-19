######################  QUESTION NO = 1 ###########################

num1 = int(input("please give me first number:-"))
num2 = int(input("please give me second number:-"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 == num2:
    print(f"{num1} is equal to {num2}")

else:
    print(f"{num2} is greater than {num1}")

######################  QUESTION NO = 2 ###########################

gen = input("please tell your gender in (M or F) -:")

if gen == "M" or "m":
    print("Hello sir ")
elif gen == "F" or "f":
    print("Hello ,ma'am")
elif gen == "other":
    print("Hello nice to have you here ")
else:
    print("please write your Gender")

######################  QUESTION NO = 3 ###########################

a = int(input("Enter your number:- "))
if a % 2==0:
    print("even number")
elif a % 2 !=0:
    print("Odd number")

######################  QUESTION NO = 4 ###########################

name=input("please tell your name :- ")
age= int(input("Please enter your age :-"))

if age >= 18:
    print(f"Hello {name} you are a valid voter")
else:
    print(f"hello{name} you can vote after{18 - age} years")

######################  QUESTION NO = 5 ###########################

year = int(input("please tell your year :- "))
if year %100 == 0 and year % 400 ==0:
     print("leap year")
elif year % 100 !=0 and year %4 ==0:
     print("leap year")
else:
     print("not a leap year")

######################  QUESTION NO = 6 ###########################

temp = int(input("please enter your temperature :-"))
if temp >= -5 and temp <=5:
    print("very cold")
elif temp >=6 and temp <=18:
    print("Cold")
elif temp >=19 and temp <=30:
    print("Hot")
else:
    print("Very Hot")







    

           


