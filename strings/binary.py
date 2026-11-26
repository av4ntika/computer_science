#Binary numbers
#to write a biary number in code
#put a 0b before the binary digits
binary_number = 0b1101
print(binary_number)
#to wirite an octal number use 0o
octal_number = 0o12
print (octal_number)
#to write a hexadecimal use 0x
hexadecimal_number = 0x12
print(hexadecimal_number)

#convert user input from binary
#to decimal
bin_num = input('enter binary number')
bin_to_dec = int(bin_num,2)
print(f'The value {bin_num} is {bin_to_dec}')

#ask the user for two binary number
#print their total
binary_number = input ('enter first number')
second_number = input ('enter second number')
binary_to_dec = int(binary_number,2)
binary_to_dec2 = int(second_number,2)
total = binary_to_dec + binary_to_dec2
print(f'The value {binary_to_dec} + {binary_to_dec2} is equal to {total}')
