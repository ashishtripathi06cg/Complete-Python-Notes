######################### FOR LOOPS ############################
 
#===<<< First Topic - Range >>>===#
# [Range () generates a sequence of numbers. Think of it as saying "count from here tp there"]

# range(10,101,1)
# range(23,57,1)
# range(46)

# for i in range(10,21,1):

#     print(i)

# for a in range(23,57,1):
#     print(a)

# for m in range(46):     #Yaha pe maine start position nhi di h to vo automatically 0 se 
#                          #start hoga and step bhi nhi h to 1 step hi chalega.
#     print(m)

# for a in range(5,51,5):
#     print(a)

# for m in range(6,61,6):
#     print(m)

#=============<<< Intresting topic >>>=================#

########## FOR LOOPS WITH NUMBER ##########

# a = int(input("please tell your number :-"))

# for a in range(a,(10*a)+1,a):
#     print(a)

########## FOR LOOPS WITH STRINGS (Range) ##########

# a ="Student"

# for i in a:
#     print(i)

# for i in range(len(a)): 
#     print(a[i])           ### method 1
#     print(f"{i} :{a[i]}") ### method 2



## <<<<<<<<<<<< Intresting Topic - Continue and Break >>>>>>>>>>>>>>

# for i in range(1,11):
#     if i ==4:
#         continue
#     print(i)

# for i in range(1,11):
#     if i ==4 or i == 7:
#         break
#     print(i)

####---------------------- Else     >>>>

for i in range(1,11):
    if i == 45:
        break
    print(i)                              #Agar break chal gya to else nhi chalega 
else:                                     #Agar break nhi chala to else chalega
    print("No break was encountered")

    

 





    

 
 
