#example
user_string = input('enter some text:')
print (user_string)
user_string_title_case = user_string.title()
print(user_string.title())

#question 1
user_string = input ('enter ur text:')
user_string_upper_case = user_string.upper()
print(user_string.upper())

#question 2
user_string = input ('enter uppercase text:')
user_string_lower_case = user_string.lower()
print(user_string.lower())

#question 3
user_string = input ('enter a string:')
user_letter = input ('enter a letter:')
user_string_count = user_string.count(user_letter)
print(user_string.count(user_letter))

#question 4
user_text = input ('enter some text:')
user_word = input ('enter ur word:')
if user_text.find (user_word) == -1:
    print ('user word is not in user text')
else:
    print (user_text.find (user_word))
    
#question 5
user_text = input ('enter a sentence:')
user_find = input ('enter the first word:')
user_word = input ('enter a replacement word:')
print (user_text.replace(user_find,user_word))

#question 6
user_string = input ('enter a string:')
if user_string.islower() == True:
    print ('ur sentence is lower case')
else:
    print ('ur user has a capital')
    
#question 7
user_string = input ('enter a sentence:')
if user_string.isupper() == True:
    print ('ur sentence is upper case')
else:
    print ('ur sentence is lower case')
    
#question 8
user_string = input ('enter a string:')
if user_string.isalnum() == True:
    print ('this is alphanumeric')
else:
    print ('ur sentance isnt alphanumeric')
    
#question 9
user_string = input ('enter a string:')
if user_string.isalpha () == True:
    print ('this is alphabetial')
else:
    print ('ur sentance isnt alphabetical')
    
#question 10
user_string = input ('enter a string:')
if user_string.isdigit () == True:
    print ('this has numbers')
else:
    print ('this has no numbers')
    
#question 11
user_string = input ('enter a string:')
user_sub = input ('enter ur sub string')
x= user_string.index(user_sub)
print (x)

#question 12
user_string = input (' enter a sentance starting and ending with a:')
print (user_string.strip('a'))