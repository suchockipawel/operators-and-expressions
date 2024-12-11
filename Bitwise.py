# convert 4999 to base 2 using python
# convert 2111 to base 2 using python
# what will be the value of 4999 & 2111
# what will be the value of 4999 | 2111

num1: int =4999
print(bin(num1))
num1_bin: str = bin(num1)
print(int(num1_bin, base=2))

num2: int =2111
print(bin(num2))
num2_bin: str = bin(num2)
print(int(num2_bin, base=2))


result_1= num1 & num2
print(result_1)

result_2= num1 | num2
print(result_2)



