# var_a = 400 var_b = '200' + '200' var_c = 400.0 var_d = 200 + 200

# what is the result of : i. var_a == var_b ii. var_a is var_b (can you explain using comments the reason for the result)

# what is the result of : i. var_a == var_c ii. var_a is var_c (can you explain using comments the reason for the result)

# what is the result of : i. var_a == var_d ii. var_a is var_d (can you explain using comments the reason for the result)

var_a = 400 
var_b = '200' + '200' 
var_c = 400.0 
var_d = 200 + 200

print(var_a == var_b) #False # differnt variable types 'int' and 'str'
print(var_a is var_b) #False # type of var_a is 'int' and type of var_b is'str'

print(var_a == var_c) #True # the same amount
print(var_a is var_c) #False # the same amount but the type of variable is different

print(var_a == var_d) #True # the same amount and type of variable:'int'
print(var_a is var_d) #True # the same amount and type of variable:'int'