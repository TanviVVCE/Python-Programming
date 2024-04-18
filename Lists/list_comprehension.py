unordered_list = [1, 2, 3]
ordered_list = [x*10 for x in unordered_list]
# print(ordered_list)

answer = [char[0] for char in ["Elie", "Tim", "Matt"]]
answer2 = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]


answer = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]

answer_1 = [str(char) for char in 'amazing' if char not in 'aeiou']

# print(answer_1)

list_123 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(val) for val in list]for list in list_123]
