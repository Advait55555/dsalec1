#decimal to b
# Function to convert decimal to binary
# def decimal_to_binary(decimal_number):
#     binary_number = []

#     # Convert decimal to binary
#     while decimal_number > 0:
#         binary_number.append(decimal_number % 2)
#         decimal_number = decimal_number // 2

#     # Print binary number in reverse order
#     print("Binary equivalent:", end=" ")
#     for digit in reversed(binary_number):
#         print(digit, end="")
#     print()

# # Driver program
# if __name__ == "__main__":
#     # Replace this value with your desired decimal number
#     decimal_number = 15

#     # Call the function to convert decimal to binary
#     decimal_to_binary(decimal_number)

# a = int(input("numero 1:"))
# b = int(input("numbero 2:"))
# c = a | b
# d = a & b
# print(f"a or b{c}")
# print(f"a n b {d} ")

#to check if number is even or odd

#if a & (a-1) == 0 ; number can be written as a power of 2

#left and right shift
# a = 13
# print(f"left shift: {a << 1}")
# print(f"right shift: {a>>1}")

#swapping w/o temp var
#first with temp:
# a = 5
# b = 7
# print("before swapping:")
# print(f"a:{a}")
# print(f"b:{b}")
# print("after swapping:")
# temp = a
# a = b
# b = temp
# print(f"a after swap:{a}")
# print(f"b after swap: {b}")

# a = 5
# b = 7
# print("before swapping:")
# print(f"a:{a}")
# print(f"b:{b}")
# print("after swapping:")
# c = a + b
# a = c-a
# b = c-b
# print(f"after swapping:{a}")
# print(f"b after swap: {b}")

# a = 9 
# b = 11
# print(a,b)
# a = a^b
# b = a^b
# a = a^b
# print(a,b)

#home work ques
#1.using bitwise operator check if num divis by 4 or not

# a = 15
# if a & 3 == 0:
#     print("it is divisible by 4")
# else:
#     print("no")

#divide num by 2 and reminder n quotient 

# print(11 >> 1)
# print(11 & 1)
# cost  = int(input("ENter the cost"))
# sp = int(input("ENter the selling price:"))
# if sp > cost :
#     print(f"You profited by {sp-cost}rupees")
# else:
#     print(f"loss by {cost-sp}rupees")

#ques 3
# x1 = int(input("enter x1:"))
# y1 = int(input("enter y1:"))
# x2 = int(input("enter x2:"))
# y2 = int(input("enter y2:"))
# x3 = int(input("enter x3:"))
# y3 = int(input("enter y3:"))
# ab = (y2-y1)/(x2-x1)
# bc = (y3-y2)/(x3-x2)
# print(ab)
# print(bc)
# if ab == bc:
#     print("they lie on the straight line")
# else:
#     print("They do not lie on a straight line")

#ques 2
# n1 = int(input("Enter n1 :"))
# o1 = input("ENter o1 :")
# n2 = int(input("Enter n2 :"))
# o2 = input("ENter o2 :")
# n3 = int(input("Enter n3 :"))
# if o1 == '+':
#     if o2 == '+':
#         print(n1 + n2 + n3)
#     elif o2 == '-':
#         print(n1+n2-n3)
#     elif o2 == '*':
#         print(n1+n2*n3)
#     else:
#         print("invalid operator")
# elif o1 == '-':
#     if o2 == '+':
#         print(n1 - n2 + n3)
#     elif o2 == '-':
#         print(n1-n2-n3)
#     elif o2 == '*':
#         print(n1-n2*n3)
#     else:
#         print("invalid operator")
# elif o1 == '*':
#     if o2 == '+':
#         print(n1 * n2 + n3)
#     elif o2 == '-':
#         print(n1*n2-n3)
#     elif o2 == '*':
#         print(n1*n2*n3)
#     else:
#         print("invalid operator")
# else:
#     print("invalid operator")
#     exit()
hardness = int(input("Enter the hardness of steel:"))
cc = float(input("Enter carbon content:"))
ts = int(input("Enter tensile strength:"))
if hardness > 50:
    i = 1
else:
    i = 0
if cc < 0.7:
    ii = 1
else:
    ii = 0
if ts > 5600:
    iii = 1
else:
    iii = 0
if i == 1 and ii == 1 and iii == 1:
    print("grade 10")
elif i == 1 and ii == 1 and iii == 0:
    print("grade 9") 
elif i == 0 and ii == 1 and iii == 1:
    print("grade 8")
elif i == 1 and ii ==0 and iii == 1:
    print("grade 7")
elif i == 1 or ii == 1 or iii == 1:
    print("grade 6") 
elif i == 0 or ii == 0 or iii == 0:
    print("grade 5")
else:
    print("invalid input")
    exit()