# from random import choice

# def tossing_coin():
#     return choice(['head','tail'])
# print(tossing_coin())
# list_evens = []
# def generate_evens():
#     for i in range(1,50):
#         if (i%2 == 0):
#             list_evens.append(i)
#     return list_evens

# print(generate_evens())

# def yell (sentence):
#     return sentence.upper()+'!'

# print(yell("go away"))

# def speak(animal = 'dog'):
#     if(animal == 'pig'):
#         return 'oink'
#     elif(animal == 'duck'):
#         return 'quack'
#     elif(animal == 'cat'):
#         return 'meow'
#     elif(animal == 'dog'):
#         return 'woof'
#     return '?'

# print(speak())


# def return_day(num):
#     week = {1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday", 7:"Saturday"}
#     day = week.get(num)
#     if day:
#         return day
#     return None

# print(return_day(18))

# def last_element(numbers):
#     if len(numbers) == 0:
#         return None
#     else:
#         return numbers[-1]
# print(last_element([1,2,3,4]))

# def number_compare(a,b):
#     if (a>b):
#         return "First is greater"
#     elif(b>a):
#         return "Second is greater"
#     return "Numbers are equal"

# def single_letter_count(str1, str2):
#     return str2.count(str1)
# print(single_letter_count('b','abcb'))

# def multiple_letter_count(str1):
#     return {char: str1.count(char)  for char in str1}

# print(multiple_letter_count('awesome'))

# def list_manipulation(alist, command, location, value):
#     if(command == 'remove' and location == 'end'):
#         return alist.pop()
#     elif(command == 'remove' and location == 'beginning'):
#         return alist.pop(0)
#     elif(command == 'add' and location == 'beginning'):
#         alist = alist.insert(0, value)
#         return alist
#     elif(command == 'add' and location == 'end'):
#         alist = alist.insert(-1,value)
#         return alist
    
# print(list_manipulation([1,2,3,4],'add','end',10))

# s = 'abc'
# s = s[::-1]
# print(s)
# def is_palidrome(str1):
#     if(str1 == str1[::-1]):
#         return True
#     return False

# print(is_palidrome('momp'))

# def frequency(alist,search):
#     return alist.count(search)

# print(frequency([1,2,3,4,4],4))
# multiple = 1
# def multiply_even_numbers(alist):
#     global multiple
#     for i in alist:
#         if(i%2 == 0):
#             multiple *= i
#     return multiple

# print(multiply_even_numbers([1,2,3,4,5]))

# blist = []
# def compact(alist):
#     for i in alist:
#         if i is True:
#             global blist
#             blist.append(i)
#     return blist
# print(compact([0,1,2,"",[], False, {}, None, "All done"]))

def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]