################ Question pratice on loops ######################
#=================== Question.1 =>

# n = int(input("Tell your number :- "))

# for i in range(n):
#     print("Hello World")

#=================== Question.2 =>

# n = int(input("Type your number :- "))

# for i in range(1,n+1):
#     print(i)

#=================== Question.3 =>

# n = int(input("Please tell your number :- "))

# for i in range(n,0,-1):
#     print(i)

#=================== Question.4 =>
# n = int(input("which table you want :-"))

# for i in range(1,11):
#     print(f"{n}*{i} = {n*i}")

#=================== Question.5 =>
# s = 0
# n = int(input("Till where you want your sum :- ")) 
                                                                            
# for i in range(1,n+1):
#     s = s + i 
#     print(s)


###============= Reasignment of variable ====================##
# a = 0
# a = a+1  
# a = a+2
# a = a+3
# a = a+4
# a = a+5 

#=================== Question.6 =>
# n = int(input("Enter which no. factorial do you want:- "))

# f=1

# for i in range(1,n+1):
#     f = f * i

# print(f)


#=================== Question.7 =>

# a = int(input("Please Enter your Number :- "))

# oddsum = 0
# evensum = 0

# for i in range(1,a+1):
#     if i % 2 == 0:
#         evensum = evensum + i
#     else:
#         oddsum = oddsum+ i

# print(f"your evensum is {evensum} and oddsum is {oddsum}")

#=================== Question.8 ==============================>>>>>>>>> Factors wale question.

# n = int(input("tell your number :- "))

# for i in range(1,n+1):
#     if n % i==0:
#         print(i)

#=================== Question.9 =============================>>>>>>>>>> Factors wale question.

# n = int(input("please tell your number :- "))


# for i in range(1,n):
#     if n % i ==0:
#         print(i)

n = int(input("please tell your number :- "))

s = 0
for i in range(1,n):
    if n % i ==0:
        s = s + i

    if s == n:
        print("Perfect number")

    else:
        print("Not a perfect number")

    
        
        
        







 





    


    








