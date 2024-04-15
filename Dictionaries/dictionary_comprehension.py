# dictionary = {num: "even" if num % 2 == 0 else "odd" for num in range(0, 101)}
# print(dictionary)

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = {list1[i]: list2[i] for i in range(len(list1))}
# print(answer)

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# # use the person variable in your answer
# answer = {person[i][0]: person[i][1] for i in range(len(person))}
# print(answer)

# answer = {char: 0 for char in 'aeiou'}
# print(answer)


answer = {char: chr(char) for char in range(65, 91)}
print(answer)
